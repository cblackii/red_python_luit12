import boto3

sess = boto3.Session(region_name='us-west-2')

s3resource = sess.resource('s3')

bucket_name = 'cbeezy-s3-training'
s3_location = {
    'LocationConstraint': 'us-west-2'
}
s3resource.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)


