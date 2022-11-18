from constants import *
import boto3

client = boto3.client("s3", aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key= AWS_SECRET_ACCESS_KEY)

bucket_name = "myyoutubev12"

location = {'LocationConstraint': "us-east-2"}

result =  client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

if result["ResponseMetadata"]["HTTPStatusCode"] == 200:
    print("Created Successfuly!!!")
else:
    print("Fail to create")

#print(result)