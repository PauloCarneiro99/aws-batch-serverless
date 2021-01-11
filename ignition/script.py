import os
import boto3


def handler(event, context):
    batch_client = boto3.client("batch")

    _ = batch_client.submit_job(
        jobName="my-first-job",
        jobQueue=(
            f"arn:aws:batch:{os.getenv('region')}:{os.getenv('account_id')}:job-queue/"
            f"{os.getenv('BATCH_JOB_QUEUE_NAME')}"
        ),
        jobDefinition=os.getenv("BATCH_JOB_DEFINITION"),
        containerOverrides={
            "command": ["python3", "script.py"],
            "environment": [{"name": "stage", "value": os.getenv("stage", "dev")}],
        },
    )

    return "Succeded"
