import matplotlib.pyplot as plt
import io
import requests


plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
plt.xlabel('Months')
plt.ylabel('Books Read')
#plt.show()

img_data = io.BytesIO()
plt.savefig(img_data, format="png")
img_data.seek(0)

from constants import *
import boto3

client = boto3.client("s3", aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY, region_name="us-east-2")

bucket_name = "myyoutubev1"

result = client.put_object(Bucket=bucket_name, Key="finalread",Body=img_data)
print(result)
