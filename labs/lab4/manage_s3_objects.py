import boto3
import sys

def list_objects(bucket_name):
    s3 = boto3.client("s3")
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if "Contents" in response:
            print(f"Objects in '{bucket_name}':")
            for obj in response["Contents"]:
                print(obj["Key"])
        else:
            print(f"No objects found in '{bucket_name}'.")
    except Exception as e:
        print(f"Error listing objects: {e}")

def delete_object(bucket_name, object_key):
    s3 = boto3.client("s3")
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Object '{object_key}' deleted from '{bucket_name}'.")
    except Exception as e:
        print(f"Error deleting object: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage_s3_objects.py <bucket_name> [object_key_to_delete]")
        sys.exit(1)

    bucket_name = sys.argv[1]

    list_objects(bucket_name)

    if len(sys.argv) == 3:
        object_key = sys.argv[2]
        delete_object(bucket_name, object_key)
