Logs into Amazon ECR

Builds a Docker image

Tags it

Pushes it to ECR

This is the exact pattern used in CI/CD pipelines (GitHub Actions, Jenkins, CodeBuild, etc.).

Prerequisites

Make sure you have:

AWS CLI configured (aws configure)

Docker installed & running

Python 3.8+

IAM permissions for ECR

boto3 installed

#pip install boto3


How This Fits in CI/CD

This script works perfectly in:

GitHub Actions

Jenkins

AWS CodeBuild

GitLab CI

You just:

Set AWS credentials as environment variables

Run python build_push_ecr.py




