import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('pen_29.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='pen_29.jpg', Body=data)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)