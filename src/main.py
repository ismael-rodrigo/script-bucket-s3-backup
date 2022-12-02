import boto3
from pathlib import Path

from downloadFiles import download_files
from settings import SETTINGS
from getFiles import get_file_folders


def main():

    client = boto3.client("s3" , aws_access_key_id= SETTINGS.aws_access_key_id ,aws_secret_access_key= SETTINGS.aws_secret_access_key , region_name= SETTINGS.region_name )

    file_names, folders = get_file_folders(client, SETTINGS.bucket_name)
    download_files(
        client,
        SETTINGS.bucket_name,
        SETTINGS.out_path,
        file_names,
        folders
    )

if __name__ == "__main__":
    main()