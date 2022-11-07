import boto3
import os
from constants import *

client = boto3.client("s3", 
                      aws_access_key_id = AWS_ACCESS_KEY_ID,
                      aws_secret_access_key = AWS_SECRET_ACCESS_KEY
                      )

bucket_name = "s3uploaddemo1"

list_files = client.list_objects(Bucket=bucket_name)['Contents']
#print(list_files)

root_path = os.getcwd()

for key in list_files:
    
    download_file_path = os.path.join(root_path, "downloads", key['Key'])
    
    client.download_file(
        Bucket = bucket_name,
        Key = key['Key'],
        Filename = download_file_path    
    )


