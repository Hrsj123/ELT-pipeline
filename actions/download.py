from boto3.session import Session

def download_file(download_path, s3_filename, access_key, secret_key):
    print('Fetching files from s3...')
    s3_bucket_name = 'store-bucket-project'
    download_path = f'{download_path}/{s3_filename}'

    session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    s3 = session.resource('s3')
    my_bucket = s3.Bucket(s3_bucket_name)

    print('client:')
    my_bucket.download_file(s3_filename, download_path)
