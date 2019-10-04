import boto3
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    bucket = s3.Bucket('test-bucket-01')
    dest_bucket = s3.Bucket('tb-bucket-02')
    print(event)# This prints the content of the event(in our case its a file from S3)
   

    for obj in bucket.objects.all():
        dest_key = obj.key
        s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': obj.bucket_name, 'Key': obj.key})# This copies the file from one bucket to another
