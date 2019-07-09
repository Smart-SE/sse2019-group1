import subprocess
import logger as log

DEFAULT_BUCKET = None
with open('s3_bucket', 'r') as f:
    DEFAULT_BUCKET = f.readlines()[0]

SEND_COMMAND_TEMPLATE = "aws s3 cp {0} {1} --acl public-read --profile={2}"
PROFILE_NAME = "sse2019-group1"


def upload_img_to_s3(file_name: str, bucket_name: str = None) -> None:
    """send image to amazon S3

    Arguments:
        file_name {str} -- uploaded file name
        bucket_name {str} -- upload to this cuket

    Returns:
        None -- return value is nothing
    """
    if not(bucket_name is None):
        send_command = SEND_COMMAND_TEMPLATE.format(bucket_name, file_name, PROFILE_NAME)
    else:
        send_command = SEND_COMMAND_TEMPLATE.format(DEFAULT_BUCKET, file_name, PROFILE_NAME)
    log.Info(send_command)
    subprocess.call(send_command, shell=True)
    return


if __name__ == '__main__':
    upload_img_to_s3("tmp.jpg")
