import boto3
from load_dotenv import load_dotenv
import os

s3_client = boto3.client('s3',
                         region_name='ap-south-1',
                         aws_access_key_id= os.environ['aws_access_id'],
                         aws_secret_access_key=os.environ[Secrect_k_Acc]
                         )


# list all s3 buckets

buckets = s3_client.list_bucktes()
for bucket in buckets['Buckets']:
    print(f"Bucket Name  : {bucket["Name"]}, Creation Date : {bucket["CreationDate"]}")