from minio import Minio
from minio.error import S3Error
import io

def file_uploader(image_bytes, image_name, bucket_name):
    client = get_client()
    create_bucket(client, bucket_name)
    upload_file(client, bucket_name, image_bytes, image_name)


def upload_file(client: Minio, bucket_name, image_bytes, image_name):
    image_bytes = io.BytesIO(image_bytes)
    # client.fput_object(bucket_name, image_name, image_bytes)
    client.put_object(bucket_name, image_name, image_bytes, length=image_bytes.getbuffer().nbytes)

def create_bucket(client, bucket_name: str):
    found = client.bucket_exists(bucket_name)
    if found: 
        return
    
    client.make_bucket(bucket_name)


def get_file_name(image_url: str) -> str:
    return image_url.split('/')[-1].split('.')[0].replace('-', '_').replace(' ', '_').replace('/', '')

def get_client():
    return Minio(endpoint='0.0.0.0:9000',                 
                 access_key='minioadmin',
                 secret_key='minioadmin',
                 secure=False)