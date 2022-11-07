import boto3
import os
from constants import *

client =  boto3.client('s3', 
                      aws_access_key_id= AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                      )

bucket_name = "s3uploaddemo1"
file_name = "mytest.csv"

root_path = os.getcwd()

download_file_path = os.path.join(root_path, "downloads", file_name)

client.download_file(
    Bucket = bucket_name,
    Key = file_name,
    Filename = download_file_path    
)
