
from constants import *
import boto3
import requests #pip install requests

client = boto3.client("s3", aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY, region_name="us-east-1")

bucket_name = "myyoutubev1"


url = client.generate_presigned_url ('get_object', Params={'Bucket':bucket_name, 'Key':"finalread"}, ExpiresIn=10)
print(url)