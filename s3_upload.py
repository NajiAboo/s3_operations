from constants import *
import boto3
import os

client =  boto3.client('s3', 
                      aws_access_key_id= AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY
                      )

root_path = os.getcwd()
print(f"root_path : {root_path}")
file_name = "insurance.csv"

file_path = os.path.join(root_path,"data", file_name)
print(f"file_path : {file_path}")

bucket_name = "s3uploaddemo1"

client.upload_file(file_path, bucket_name, "mytest.csv")