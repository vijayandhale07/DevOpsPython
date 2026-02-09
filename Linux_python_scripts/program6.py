#4 Real DevOps Examples
# List EC2 instances


import boto3 

ec2 = boto3.clinet("ec2")

response = ec2.describe_instances()

for reservation in response["Reservations"]:
  for instance in reservation["Instances"]:
	print(instance["InstanceId"],instance["State"]["Name"])

