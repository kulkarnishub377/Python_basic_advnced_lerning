import os
import shutil
import uuid
import aiofiles
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_file_locally(file: UploadFile) -> str:
    """
    Saves an uploaded file to the local disk asynchronously.
    Returns the generated unique filename.
    """
    # Generate unique filename to prevent overwrites
    file_ext = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{file_ext}"
    
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    # Save file asynchronously in chunks
    async with aiofiles.open(file_path, 'wb') as out_file:
        while content := await file.read(1024 * 1024):  # Read in 1MB chunks
            await out_file.write(content)
            
    return unique_filename

def get_all_local_files() -> list:
    """Returns a list of all filenames currently in the upload directory."""
    if not os.path.exists(UPLOAD_DIR):
        return []
    return os.listdir(UPLOAD_DIR)

# Example of how S3 would be implemented:
"""
import boto3

s3_client = boto3.client('s3', aws_access_key_id='...', aws_secret_access_key='...')

async def save_file_to_s3(file: UploadFile) -> str:
    unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
    s3_client.upload_fileobj(file.file, "my-bucket-name", unique_filename)
    return unique_filename
"""
