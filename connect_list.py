import boto3

client = boto3.client('s3', 
                      aws_access_key_id="AKIAV6E5X54W5KVYY46X",
                      aws_secret_access_key="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"
                      )

response = client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])

#print(response)

