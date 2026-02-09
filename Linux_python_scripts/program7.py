# Start an EC2 instance with python program

import boto3 

ec2 = boto3.client("ec2")

ec2.start_instances(InstanceIds=["instance_id"])

ec2.start_instances(InstanceIds=["i-1234567890abcdef0"])
print("Instance started")

#####################################

######### Stop an EC2 instance #################

ec2.stop_instances(InstanceIds=["instace_id"])

print("Instance stopped...")


#########################################

######### Create a s3 bucket ###############

import boto3 

s3 = boto3.client("s3")

s3.create_bucket(
    Bucket="my-devops-bucket-123",
    CreateBucketConfiguration={"LocationConstraint": "ap-south-1"}   
)

print("Bucket created")

################################################

###### Upload file to S3 ##########


s3 = boto3.client("s3")

s3.upload_file("test.txt","my-devops-bucket-123","test.txt")
print("Uploaded successfully")

################################################

# Real DevOps Automation Script


#### Auto- stop EC2 instance at night....

import boto3 

ec2 = boto3.client("ec2")

instances = ec2.describe_instances()

for r in instances["Reservations"]:
    for i in r["Instances"]:
        if i["State"]["Name"]== "running"
            ec2.stop_instances(InstanceIds=[i["InstaceId"]])
            print(f"Stopped {i['InstanceId']}")
            
           
           
           
#6 Best Practices in DevOps

# Use IAM roles instead of hard-coding keys
# Add exception handling 
# Use tages tp filter resources 
# Schedule scripts using cron or jenkins

# Example with tag filter: 


ec2.describe_instances(
        Filters=[{"Name":"tag:Env","Values":["Dev]}]
)
           

