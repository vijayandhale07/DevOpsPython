with open("aws_s3_bucket_create.py", "r") as file:
    code = file.read()
    if "boto3" in code:
        print("The code uses the boto3 library to interact with AWS services.")