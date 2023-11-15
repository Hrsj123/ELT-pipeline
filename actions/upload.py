import os
from boto3.s3.transfer import S3Transfer
import boto3

def upload_file(access_key, secret_key):
    print('Uploading files...')
    # s3_filename = 'missed_shipping_limit_orders.csv'      # Name of the file which is uploaded!
    s3_bucket_name = 'store-bucket-project'
    filepath = './Output/'
    client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    print('client:')
    transfer = S3Transfer(client)

    print('Transfering to: ' + s3_bucket_name)

    # Define function to scan through the Spark output uploadDirectory,
    # identify csv files, and upload them to the S3 bucket
    def uploadDirectory(filepath, s3_bucket_name):
        for root, dirs, files in os.walk(filepath):
            for file in files:
                # Transfer only csv files
                if file.endswith('csv'):
                    transfer.upload_file(
                        os.path.join(root, file),
                        s3_bucket_name,
                        f"Clean_Data/{file}"
                    )

    uploadDirectory(filepath=filepath, s3_bucket_name=s3_bucket_name)