#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A CLI for parsing DMARC reports"""


from argparse import ArgumentParser
from glob import glob
import logging
from collections import OrderedDict
import json
from ssl import CERT_NONE, create_default_context

from parsedmarc import IMAPError, get_dmarc_reports_from_inbox, \
    parse_report_file, elastic, kafkaclient, splunk, save_output, \
    watch_inbox, email_results, SMTPError, ParserError, __version__

logger = logging.getLogger("parsedmarc")


def _main():
    """Called when the module is executed"""

    def process_reports(reports_):
        output_str = "{0}\n".format(json.dumps(reports_,
                                               ensure_ascii=False,
                                               indent=2))
        if not args.silent:
            print(output_str)
        if args.kafka_hosts:
            try:
                kafka_client = kafkaclient.KafkaClient(
                    args.kafka_hosts,
                    username=args.kafka_username,
                    password=args.kafka_password
                )
            except Exception as error_:
                logger.error("Kafka Error: {0}".format(error_.__str__()))
        if args.save_aggregate:
            for report in reports_["aggregate_reports"]:
                try:
                    if args.elasticsearch_host:
                        elastic.save_aggregate_report_to_elasticsearch(
                            report,
                            index_suffix=args.elasticsearch_index_suffix,
                            monthly_indexes=args.elasticsearch_monthly_indexes)
                except elastic.AlreadySaved as warning:
                    logger.warning(warning.__str__())
                except elastic.ElasticsearchError as error_:
                    logger.error("Elasticsearch Error: {0}".format(
                        error_.__str__()))
                try:
                    if args.kafka_hosts:
                        kafka_client.save_aggregate_reports_to_kafka(
                            report, kafka_aggregate_topic)
                except Exception as error_:
                    logger.error("Kafka Error: {0}".format(
                         error_.__str__()))
            if args.hec:
                try:
                    aggregate_reports_ = reports_["aggregate_reports"]
                    if len(aggregate_reports_) > 0:
                        hec_client.save_aggregate_reports_to_splunk(
                            aggregate_reports_)
                except splunk.SplunkError as e:
                    logger.error("Splunk HEC error: {0}".format(e.__str__()))
        if args.save_forensic:
            for report in reports_["forensic_reports"]:
                try:
                    if args.elasticsearch_host:
                        elastic.save_forensic_report_to_elasticsearch(
                            report,
                            index_suffix=args.elasticsearch_index_suffix,
                            monthly_indexes=args.elasticsearch_monthly_indexes)
                except elastic.AlreadySaved as warning:
                    logger.warning(warning.__str__())
                except elastic.ElasticsearchError as error_:
                    logger.error("Elasticsearch Error: {0}".format(
                        error_.__str__()))
                try:
                    if args.kafka_hosts:
                        kafka_client.save_forensic_reports_to_kafka(
                            report, kafka_forensic_topic)
                except Exception as error_:
                    logger.error("Kafka Error: {0}".format(
                        error_.__str__()))
            if args.hec:
                try:
                    forensic_reports_ = reports_["forensic_reports"]
                    if len(forensic_reports_) > 0:
                        hec_client.save_forensic_reports_to_splunk(
                            forensic_reports_)
                except splunk.SplunkError as e:
                    logger.error("Splunk HEC error: {0}".format(e.__str__()))

    arg_parser = ArgumentParser(description="Parses DMARC reports")
    arg_parser.add_argument("file_path", nargs="*",
                            help="one or more paths to aggregate or forensic "
                                 "report files or emails")
    strip_attachment_help = "remove attachment payloads from forensic " \
                            "report output"
    arg_parser.add_argument("--strip-attachment-payloads",
                            help=strip_attachment_help, action="store_true")
    arg_parser.add_argument("-o", "--output",
                            help="write output files to the given directory")
    arg_parser.add_argument("-n", "--nameservers", nargs="+",
                            help="nameservers to query "
                                 "(default is Cloudflare's nameservers)")
    arg_parser.add_argument("-t", "--timeout",
                            help="number of seconds to wait for an answer "
                                 "from DNS (default: 6.0)",
                            type=float,
                            default=6.0)
    arg_parser.add_argument("-H", "--host",
                            help="an IMAP hostname or IP address")
    arg_parser.add_argument("-u", "--user", help="an IMAP user")
    arg_parser.add_argument("-p", "--password", help="an IMAP password")
    arg_parser.add_argument("--imap-port", default=None, help="an IMAP port")
    arg_parser.add_argument("--imap-skip-certificate-verification",
                            action="store_true",
                            default=False,
                            help="skip certificate verification for IMAP")
    arg_parser.add_argument("--imap-no-ssl", action="store_true",
                            default=False,
                            help="do not use SSL/TLS when connecting to IMAP")
    arg_parser.add_argument("-r", "--reports-folder", default="INBOX",
                            help="the IMAP folder containing the reports\n"
                                 "(default: INBOX)")
    arg_parser.add_argument("-a", "--archive-folder",
                            help="specifies the IMAP folder to move "
                                 "messages to after processing them\n"
                                 "(default: Archive)",
                            default="Archive")
    arg_parser.add_argument("-d", "--delete",
                            help="delete the reports after processing them",
                            action="store_true", default=False)

    arg_parser.add_argument("-E", "--elasticsearch-host", nargs="*",
                            help="une or more Elasticsearch "
                                 "hostnames or URLs to use (e.g. "
                                 "localhost:9200)")
    arg_parser.add_argument("--elasticsearch-index-suffix",
                            help="append this suffix to the "
                                 "dmarc_aggregate and dmarc_forensic "
                                 "Elasticsearch index names, joined by _")
    arg_parser.add_argument("--elasticsearch-use-ssl", default=False,
                            action="store_true",
                            help="Use SSL when connecting to Elasticsearch")
    arg_parser.add_argument("--elasticsearch-ssl-cert-path", default=None,
                            help="Path to the Elasticsearch SSL certificate")
    arg_parser.add_argument("--elasticsearch-monthly-indexes",
                            action="store_true", default=False,
                            help="Use monthly Elasticsearch indexes instead "
                                 "of daily indexes")
    arg_parser.add_argument("--hec", help="the URL to a Splunk HTTP Event "
                                          "Collector (HEC)")
    arg_parser.add_argument("--hec-token", help="the authorization token for "
                                                "a Splunk "
                                                "HTTP Event Collector (HEC)")
    arg_parser.add_argument("--hec-index", help="the index to use when "
                                                "sending events to the "
                                                "Splunk HTTP Event Collector "
                                                "(HEC)")
    arg_parser.add_argument("--hec-skip-certificate-verification",
                            action="store_true",
                            default=False,
                            help="skip certificate verification for Splunk "
                                 "HEC")
    arg_parser.add_argument("-K", "--kafka-hosts", nargs="*",
                            help="a list of one or more Kafka hostnames")
    arg_parser.add_argument("--kafka-username",
                            help='an optional Kafka username')
    arg_parser.add_argument("--kafka-password",
                            help="an optional Kafka password")
    arg_parser.add_argument("--kafka-use-ssl",
                            action="store_true",
                            help="use SSL/TLS to connect to Kafka "
                                 "(implied when --kafka-username or "
                                 "--kafka-password are provided)")
    arg_parser.add_argument("--kafka-aggregate-topic",
                            help="the Kafka topic to publish aggregate "
                            "reports to (default: dmarc_aggregate)",
                            default="dmarc_aggregate")
    arg_parser.add_argument("--kafka-forensic_topic",
                            help="the Kafka topic to publish forensic reports"
                            " to (default: dmarc_forensic)",
                            default="dmarc_forensic")
    arg_parser.add_argument("--save-aggregate", action="store_true",
                            default=False,
                            help="save aggregate reports to search indexes")
    arg_parser.add_argument("--save-forensic", action="store_true",
                            default=False,
                            help="save forensic reports to search indexes")
    arg_parser.add_argument("-O", "--outgoing-host",
                            help="email the results using this host")
    arg_parser.add_argument("-U", "--outgoing-user",
                            help="email the results using this user")
    arg_parser.add_argument("-P", "--outgoing-password",
                            help="email the results using this password")
    arg_parser.add_argument("--outgoing-port",
                            help="email the results using this port")
    arg_parser.add_argument("--outgoing-ssl",
                            help="use SSL/TLS instead of STARTTLS (more "
                                 "secure, and required by some providers, "
                                 "like Gmail)")
    arg_parser.add_argument("-F", "--outgoing-from",
                            help="email the results using this from address")
    arg_parser.add_argument("-T", "--outgoing-to", nargs="+",
                            help="email the results to these addresses")
    arg_parser.add_argument("-S", "--outgoing-subject",
                            help="email the results using this subject")
    arg_parser.add_argument("-A", "--outgoing-attachment",
                            help="email the results using this filename")
    arg_parser.add_argument("-M", "--outgoing-message",
                            help="email the results using this message")
    arg_parser.add_argument("-w", "--watch", action="store_true",
                            help="use an IMAP IDLE connection to process "
                                 "reports as they arrive in the inbox")
    arg_parser.add_argument("--test",
                            help="do not move or delete IMAP messages",
                            action="store_true", default=False)
    arg_parser.add_argument("-s", "--silent", action="store_true",
                            help="only print errors and warnings")
    arg_parser.add_argument("--debug", action="store_true",
                            help="print debugging information")
    arg_parser.add_argument("--log-file", default=None,
                            help="output logging to a file")
    arg_parser.add_argument("-v", "--version", action="version",
                            version=__version__)

    aggregate_reports = []
    forensic_reports = []

    args = arg_parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    logger.setLevel(logging.WARNING)

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    if args.log_file:
        fh = logging.FileHandler(args.log_file)
        formatter = logging.Formatter(
            '%(asctime)s - '
            '%(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    if args.host is None and len(args.file_path) == 0:
        arg_parser.print_help()
        exit(1)

    if args.save_aggregate or args.save_forensic:
        if (args.elasticsearch_host is None and args.hec is None
                and args.kafka_hosts is None):
            args.elasticsearch_host = ["localhost:9200"]
        try:
            if args.elasticsearch_host:
                es_aggregate_index = "dmarc_aggregate"
                es_forensic_index = "dmarc_forensic"
                if args.elasticsearch_index_suffix:
                    suffix = args.elasticsearch_index_suffix
                    es_aggregate_index = "{0}_{1}".format(
                        es_aggregate_index, suffix)
                    es_forensic_index = "{0}_{1}".format(
                        es_forensic_index, suffix)
                elastic.set_hosts(args.elasticsearch_host,
                                  args.elasticsearch_use_ssl,
                                  args.elasticsearch_ssl_cert_path)
                elastic.migrate_indexes(aggregate_indexes=[es_aggregate_index],
                                        forensic_indexes=[es_forensic_index])
        except elastic.ElasticsearchError as error:
            logger.error("Elasticsearch Error: {0}".format(error.__str__()))
            exit(1)

    if args.hec:
        if args.hec_token is None or args.hec_index is None:
            logger.error("HEC token and HEC index are required when "
                         "using HEC URL")
            exit(1)

        verify = True
        if args.hec_skip_certificate_verification:
            verify = False
        hec_client = splunk.HECClient(args.hec, args.hec_token,
                                      args.hec_index,
                                      verify=verify)

    kafka_aggregate_topic = args.kafka_aggregate_topic
    kafka_forensic_topic = args.kafka_forensic_topic

    file_paths = []
    for file_path in args.file_path:
        file_paths += glob(file_path)
    file_paths = list(set(file_paths))

    for file_path in file_paths:
        try:
            sa = args.strip_attachment_payloads
            file_results = parse_report_file(file_path,
                                             nameservers=args.nameservers,
                                             timeout=args.timeout,
                                             strip_attachment_payloads=sa)
            if file_results["report_type"] == "aggregate":
                aggregate_reports.append(file_results["report"])
            elif file_results["report_type"] == "forensic":
                forensic_reports.append(file_results["report"])

        except ParserError as error:
            logger.error("Failed to parse {0} - {1}".format(file_path,
                                                            error))

    if args.host:
        try:
            if args.user is None or args.password is None:
                logger.error("user and password must be specified if"
                             "host is specified")

            rf = args.reports_folder
            af = args.archive_folder
            ns = args.nameservers
            sa = args.strip_attachment_payloads
            ssl = True
            ssl_context = None
            if args.imap_skip_certificate_verification:
                logger.debug("Skipping IMAP certificate verification")
                ssl_context = create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = CERT_NONE
            if args.imap_no_ssl:
                ssl = False
            reports = get_dmarc_reports_from_inbox(host=args.host,
                                                   port=args.imap_port,
                                                   ssl=ssl,
                                                   ssl_context=ssl_context,
                                                   user=args.user,
                                                   password=args.password,
                                                   reports_folder=rf,
                                                   archive_folder=af,
                                                   delete=args.delete,
                                                   nameservers=ns,
                                                   test=args.test,
                                                   strip_attachment_payloads=sa
                                                   )

            aggregate_reports += reports["aggregate_reports"]
            forensic_reports += reports["forensic_reports"]

        except IMAPError as error:
            logger.error("IMAP Error: {0}".format(error.__str__()))
            exit(1)

    results = OrderedDict([("aggregate_reports", aggregate_reports),
                           ("forensic_reports", forensic_reports)])

    if args.output:
        save_output(results, output_directory=args.output)

    process_reports(results)

    if args.outgoing_host:
        if args.outgoing_from is None or args.outgoing_to is None:
            logger.error("--outgoing-from and --outgoing-to must "
                         "be provided if --outgoing-host is used")
            exit(1)

        try:
            email_results(results, args.outgoing_host, args.outgoing_from,
                          args.outgoing_to, use_ssl=args.outgoing_ssl,
                          user=args.outgoing_user,
                          password=args.outgoing_password,
                          subject=args.outgoing_subject)
        except SMTPError as error:
            logger.error("SMTP Error: {0}".format(error.__str__()))
            exit(1)

    if args.host and args.watch:
        logger.info("Watching for email - Quit with ctrl-c")
        ssl = True
        ssl_context = None
        if args.imap_skip_certificate_verification:
            logger.debug("Skipping IMAP certificate verification")
            ssl_context = create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = CERT_NONE
        if args.imap_no_ssl:
            ssl = False
        try:
            sa = args.strip_attachment_payloads
            watch_inbox(args.host, args.user, args.password, process_reports,
                        port=args.imap_port, ssl=ssl, ssl_context=ssl_context,
                        reports_folder=args.reports_folder,
                        archive_folder=args.archive_folder, delete=args.delete,
                        test=args.test, nameservers=args.nameservers,
                        dns_timeout=args.timeout, strip_attachment_payloads=sa)
        except IMAPError as error:
            logger.error("IMAP error: {0}".format(error.__str__()))
            exit(1)


if __name__ == "__main__":
    _main()
