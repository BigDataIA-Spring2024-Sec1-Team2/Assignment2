import os
import boto3

def upload_text_files_to_s3(local_path, bucket_name, s3_folder):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Iterate through all files in the local directory
    for filename in os.listdir(local_path):
        if filename.endswith(".txt"):
            local_file_path = os.path.join(local_path, filename)
            s3_object_key = f"{s3_folder}/{filename}"

            # Check if the file already exists in S3
            try:
                s3.head_object(Bucket=bucket_name, Key=s3_object_key)
                print(f"File {filename} already exists in S3. Overwriting...")
            except Exception as e:
                # If the file doesn't exist, upload it
                try:
                    s3.upload_file(local_file_path, bucket_name, s3_object_key)
                    print(f"File {filename} uploaded successfully to S3: s3://{bucket_name}/{s3_object_key}")
                except Exception as upload_error:
                    print(f"Error uploading file {filename} to S3: {upload_error}")

# Replace these values with your actual AWS credentials, local path, bucket name, and S3 folder
# aws_access_key = 'your_access_key'
# aws_secret_key = 'your_secret_key'
local_path = 'C:/Users/aptea/OneDrive/Documents/NEU/Sem6/BDIA/Assignment 2'
s3_bucket_name = 'cfa-pdfs'
s3_folder_name = 'pypdf'

# Upload only new text files or overwrite existing ones in the specified S3 folder
upload_text_files_to_s3(local_path, s3_bucket_name, s3_folder_name)
