import subprocess
import boto3
import base64
import sys

AWS_REGION = "us-east-1"
AWS_ACCOUNT_ID = "123456789012"
ECR_REPO_NAME = "my-app"
IMAGE_TAG = "latest"
DOCKERFILE_PATH = "."  # path where Dockerfile exists


def run_cmd(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit("Command failed")


def ecr_login():
    ecr = boto3.client("ecr", region_name=AWS_REGION)
    auth_data = ecr.get_authorization_token()["authorizationData"][0]

    token = base64.b64decode(auth_data["authorizationToken"]).decode()
    username, password = token.split(":")

    registry = auth_data["proxyEndpoint"]

    run_cmd(
        f"docker login -u {username} -p {password} {registry}"
    )


def build_image():
    run_cmd(
        f"docker build -t {ECR_REPO_NAME}:{IMAGE_TAG} {DOCKERFILE_PATH}"
    )


def tag_image():
    ecr_uri = f"{AWS_ACCOUNT_ID}.dkr.ecr.{AWS_REGION}.amazonaws.com/{ECR_REPO_NAME}:{IMAGE_TAG}"
    run_cmd(
        f"docker tag {ECR_REPO_NAME}:{IMAGE_TAG} {ecr_uri}"
    )
    return ecr_uri


def push_image(ecr_uri):
    run_cmd(
        f"docker push {ecr_uri}"
    )


if __name__ == "__main__":
    print("🔐 Logging into ECR...")
    ecr_login()

    print("🐳 Building Docker image...")
    build_image()

    print("🏷️ Tagging image...")
    image_uri = tag_image()

    print("🚀 Pushing image to ECR...")
    push_image(image_uri)

    print(f"✅ Image pushed successfully: {image_uri}")
