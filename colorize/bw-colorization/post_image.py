import boto3

bucket_name = 'sse02-group1-fridgepics'
source_file_name = 'tmp.jpg'
target_file_name = 'tmp_colorized.jpg'

s3 = boto3.client('s3')
s3.upload_file(target_file_name,bucket_name,target_file_name,ExtraArgs={'ACL':'public-read'})
s3.delete_object(Bucket=bucket_name, Key=source_file_name)
