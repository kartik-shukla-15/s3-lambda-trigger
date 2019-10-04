Serverless.yml - 

Two S3 buckets are configured along with the lambda function with s3 event
The SNS Topic is also configured in the file.

The buckets are configured as:-
Type: AWS::S3::Bucket
Properties: 
  BucketName:"Incoming"

Type: AWS::S3::Bucket
Properties: 
  BucketName:"Processed"

funtion are configured as:-
functions:

  bucket:
    handler: lambda_handler.event
    name: ${self:custom.stack_name}-bucket
    events:
      - s3:
          bucket: ${self:custom.s3_bucket}
          event: s3:ObjectCreated:*
          rules:
            - prefix: ${self:custom.s3_key_base}
      - s3:
          bucket: ${self:custom.s3_bucket}
          event: s3:ObjectCreated:*
          rules:
            - prefix: ${self:custom.s3_key_base}

Topic is configured as:-
Type: AWS::SNS::Topic
Properties: 
  DisplayName: 'GitHub'
  KmsMasterKeyId: '61982e77-69bc-4a02-8cc8-df0e611a5c5d'
  Subscription: 
    - lambda_handler
  TopicName: 'github'
  
