from constants import *
import boto3

client = boto3.client("s3", aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY)

bucket_name = "myyoutubev1"

response = client.delete_bucket(Bucket=bucket_name)

print(response)

# list_objects = client.list_objects(Bucket=bucket_name)['Contents']
# #print(list_objects)

# object_list = []

# for data in list_objects:
#     object_list.append({'Key': data.get('Key')})
    
# #print(object_list)

# if object_list:
#     response = client.delete_objects(Bucket=bucket_name, Delete={'Objects': object_list})

# print(response)