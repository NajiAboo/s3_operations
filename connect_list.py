import boto3
from constants import *

client = boto3.client('s3', 
                      aws_access_key_id= AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                      )

response = client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])

#print(response)

