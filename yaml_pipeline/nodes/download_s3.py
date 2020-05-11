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

    # Skip downloading if flag set
    skip_if_exists = settings['skip_if_exists'] if 'skip_if_exists' in settings else False

    if skip_if_exists and path.exists(settings['local_path']):
        return dfs

    # Set credentials if exist
    key = settings['aws_access_key_id'] if 'access_key_id' in settings else None
    secret = settings['aws_secret_access_key'] if 'aws_secret_access_key' in settings else None

    # Download
    S3FileSystem(key=key, secret=secret) \
        .get(settings['remote_path'], settings['local_path'])

    return dfs
