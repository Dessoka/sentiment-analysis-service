# Sentiment Analysis Service

This project deploys a Flask-based sentiment analysis API using a pre-trained Hugging Face NLP model. The application is containerized with Docker, pushed to Amazon Elastic Container Registry (ECR), and deployed using AWS App Runner. GitHub Actions is used for CI/CD automation.

## Project Structure

```text
sentiment-analysis-service/
├── app.py
├── model.py
├── cli.py
├── requirements.txt
├── Dockerfile
├── Makefile
├── .github/workflows/ci-cd.yml
└── README.md
```

## Local Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit:

```bash
http://127.0.0.1:5000/
```

## Test Prediction Endpoint

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"I really enjoyed this product"}'
```

Or use the CLI:

```bash
python cli.py "I really enjoyed this product"
```

## Docker Commands

Build the image:

```bash
docker build -t sentiment-analysis-service .
```

Run the container:

```bash
docker run -p 5000:5000 sentiment-analysis-service
```

## AWS ECR Commands

Create ECR repository:

```bash
aws ecr create-repository --repository-name sentiment-analysis-service --region us-east-1
```

Authenticate Docker:

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

Tag image:

```bash
docker tag sentiment-analysis-service:latest <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/sentiment-analysis-service:latest
```

Push image:

```bash
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/sentiment-analysis-service:latest
```

## GitHub Secrets Required

Add these secrets in GitHub repository settings:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_ACCOUNT_ID`

## Deployment

Use AWS App Runner and select the ECR image:

```text
<AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/sentiment-analysis-service:latest
```

App Runner will provide a public HTTPS service URL.
