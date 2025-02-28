import boto3
import sys

def create_bucket(bucket_name, region="us-east-1"):
    s3 = boto3.client("s3", region_name=region)
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating bucket: {e}")

def upload_file(bucket_name, file_path, object_name=None):
    s3 = boto3.client("s3")
    object_name = object_name or file_path
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded successfully to '{bucket_name}/{object_name}'")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_s3_bucket.py <bucket_name> <file_path>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    file_path = sys.argv[2]
    
    create_bucket(bucket_name)
    upload_file(bucket_name, file_path)
