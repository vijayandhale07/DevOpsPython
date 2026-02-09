# Basic boto3 scripts 
# boto3 install and Configure 
# install boto3

# pip install boto3 

# Configure AWS credentials 

#aws configure 

#Enter AWS access key 
#Secret Key
#Region (example: ap-south-1)
#Output format(json)

#Credentials stored in:

#~/.aws/credentials


Basic boto3 Structure 

import boto3

#client = boto3.client("service_name")

ec2 = boto3.client("ec2")



