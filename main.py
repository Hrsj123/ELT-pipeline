import os
from dotenv import load_dotenv
load_dotenv()

from actions.download import download_file
from actions.operations import operations
from actions.upload import upload_file

if __name__ == '__main__':
    access_key = os.getenv('ACCESS_KEY')    
    secret_key = os.getenv('SECRET_KEY')

    data_path = './Data'
    file_name = 'brazilian-ecommerce.zip'

    # Pipeline process!
    download_file(data_path, file_name, access_key, secret_key)
    operations(data_path, file_name)
    upload_file(access_key, secret_key)