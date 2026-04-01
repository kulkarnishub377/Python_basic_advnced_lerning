# 84 - Serverless AWS Lambda API (FastAPI + Mangum)

This project demonstrates how to deploy a full **FastAPI** application as a serverless function on **AWS Lambda** using the AWS Serverless Application Model (SAM).

Instead of maintaining a server that is always running, AWS Lambda runs your code only when a request comes in, scaling automatically from 0 to 1000s of requests per second.

## Key Concepts
- **Mangum:** An adapter that translates AWS API Gateway events into ASGI standard events that FastAPI can understand.
- **AWS SAM (`template.yaml`):** Infrastructure-as-code configuration specifying how the Lambda function and API Gateway should be provisioned.

## Local Development

If you just want to run the code locally as a standard HTTP server:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deployment Simulator (AWS SAM CLI)

If you have Docker and the AWS SAM CLI installed, you can simulate the AWS Lambda environment locally:
```bash
sam build
sam local start-api
```
