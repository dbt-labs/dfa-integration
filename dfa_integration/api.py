from datetime import datetime
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
from httplib2 import Http
from time import sleep

from dfa_integration.logger import GLOBAL_LOGGER as logger


class APIClient:
    def __init__(self, config):
        self.credentials = GoogleCredentials(
            None,
            client_id=config.get('client_id'),
            client_secret=config.get('client_secret'),
            refresh_token=config.get('refresh_token'),
            token_expiry=None,
            token_uri="https://accounts.google.com/o/oauth2/token",
            user_agent=config.get('user_agent')
        )

        self.refresh_credentials()

    def refresh_credentials(self):
        http = self.credentials.authorize(Http())
        self.credentials.refresh(http)

    def get_report(self, profile_id, report_id):
        service = build('dfareporting', 'v3.0', credentials=self.credentials)

        logger.info("Running report {} for profile {}...".format(
            report_id,
            profile_id))

        run = service.reports().run(profileId=profile_id,
                                    reportId=report_id).execute()

        file_id = run.get('id')

        running = True

        while running:
            f = service.reports().files().get(profileId=profile_id,
                                              reportId=report_id,
                                              fileId=file_id).execute()

            if f.get('status') == 'PROCESSING':
                logger.info("> Report is still processing, retry in 5s.")
                sleep(5)
            else:
                running = False

        logger.info("Completed with status '{}'.".format(f.get('status')))

        file_value = service.reports().files().get_media(
            profileId=profile_id,
            reportId=report_id,
            fileId=file_id).execute().decode('utf-8')

        # the data comes in with some garbage on the first few, and
        # last, lines. remove it
        split = file_value.split('\n')
        header_lines = split[0:9]
        data_lines = split[9:]
        data_lines = data_lines[:-2]

        generated_time = datetime.strptime(
            # 2/16/18 1:42 PM
            header_lines[2].split(',')[1],
            '%m/%d/%y %I:%M %p'
        )

        # 2/1/18 - 2/16/18
        time_range = header_lines[5].split(',')[1]

        output = []
        for index, line in enumerate(data_lines):
            if index == 0:
                output.append(
                    '{},{},{}'.format(line, 'generated_time', 'time_range'))
            else:
                output.append(
                    '{},{},{}'.format(line, generated_time, time_range))

        return (
            file_id,
            '\n'.join(output).encode('utf-8'),
        )
