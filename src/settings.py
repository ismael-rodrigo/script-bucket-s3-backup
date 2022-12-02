import os
from decouple import config

class Settings():
    aws_access_key_id = config('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
    region_name = config('AWS_REGION_NAME')
    bucket_name = config('AWS_BUCKET_NAME')
    out_path = "out"

SETTINGS = Settings()