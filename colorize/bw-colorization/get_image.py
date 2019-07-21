import boto3

bucket_name = 'sse02-group1-fridgepics'
object_name = 'tmp.jpg'

s3 = boto3.client('s3')
s3_object_exists_waiter = s3.get_waiter('object_exists')
s3_object_exists_waiter.wait(Bucket=bucket_name, Key=object_name)
s3.download_file(bucket_name, object_name, object_name)

