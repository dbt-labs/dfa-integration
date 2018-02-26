import boto3

from dfa_integration.logger import GLOBAL_LOGGER as logger


class S3Client:

    def __init__(self, config):
        self.config = config
        self.client = boto3.client('s3')

    def upload_stream(self, path, stream):
        result = self.client.put_object(
            Body=stream,
            Bucket=self.config.get('s3_bucket'),
            Key=path)

        return result
