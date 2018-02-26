import argparse

from datetime import datetime

from dfa_integration.api import APIClient
from dfa_integration.config import load_config
from dfa_integration.s3 import S3Client
from dfa_integration.state import incorporate, save_state, load_state

from dfa_integration.logger import GLOBAL_LOGGER as logger


def do_sync(args):
    config = load_config(args.config)
    state = load_state(args.state)

    dfa_client = APIClient(config)
    s3_client = S3Client(config)

    for report in config.get('reports'):
        profile_id = report.get('profile_id')
        report_id = report.get('report_id')

        file_id, data = dfa_client.get_report(profile_id, report_id)

        path = '{}/{}/{}.csv'.format(profile_id, report_id, file_id)

        s3_client.upload_stream(path, data)

        state = incorporate(state, profile_id, report_id, datetime.now())
        state = save_state(state, args.state)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-c', '--config', help='Config file', required=True)
    parser.add_argument(
        '-s', '--state', help='State file')

    args = parser.parse_args()

    try:
        do_sync(args)
    except RuntimeError:
        logger.fatal("Run failed.")
        exit(1)


if __name__ == '__main__':
    main()
