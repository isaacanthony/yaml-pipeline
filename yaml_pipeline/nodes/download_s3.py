"""Download file from s3"""
from os import path


def run(dfs: dict, settings: dict) -> dict:
    """Download file from s3"""
    # Only import s3fs if node is called.
    # Assumes calling party has s3fs installed.
    from s3fs import S3FileSystem

    for col in ['remote_path', 'local_path']:
        if col not in settings:
            raise Exception(f"Missing {col} param")

    # Add prefixes
    if 's3_prefix' in settings:
        remote_path = settings['s3_prefix'] + settings['remote_path']
    else:
        remote_path = settings['remote_path']

    if 'local_prefix' in settings:
        local_path = settings['local_prefix'] + settings['local_path']
    else:
        local_path = settings['local_path']

    # Skip downloading if flag set
    skip_if_exists = settings['skip_if_exists'] if 'skip_if_exists' in settings else False

    if skip_if_exists and path.exists(local_path):
        if 'logger' in settings:
            settings['logger'].info('File already downloaded')

        return dfs

    # Set credentials if exist
    key = settings['aws_access_key_id'] if 'aws_access_key_id' in settings else None
    secret = settings['aws_secret_access_key'] if 'aws_secret_access_key' in settings else None

    # Download
    s3_client = S3FileSystem(key=key, secret=secret)

    # Log file size if logging
    if 'logger' in settings:
        file_size = s3_client.du(remote_path)
        file_size = _file_size_to_str(file_size)
        settings['logger'].info("File size is %s", file_size)

    s3_client.get(remote_path, local_path)
    return dfs


def _file_size_to_str(file_size: int) -> str:
    """File size int to str"""
    if file_size >= 1e9:
        return f"{round(file_size / 1e9, 1)}gb"

    if file_size >= 1e6:
        return f"{round(file_size / 1e6, 1)}mb"

    if file_size >= 1e3:
        return f"{round(file_size / 1e3, 1)}kb"

    return f"{file_size}bytes"
