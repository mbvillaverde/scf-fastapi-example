# FastAPI Application Example for Serverless Container Framework

This example leverages the use of [Serverless Container Framework (SCF)](https://serverless.com/containers/docs) to build and deploy a basic FastAPI application in AWS Lambda or ECS Fargate.

This application sets up a basic routes which includes a health checking route and basic 404 routes. All images and styles are copied from the official [Serverless Container Framework Github](https://github.com/serverless/containers).

## Prerequisites

This project assumes that you already have an [AWS Account](https://console.aws.amazon.com/console/home) and [Serverless Account](https://app.serverless.com/) already logged-in inside your browser.

If you are using VSCode or Cursor as your IDE, you will be needing to add the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

Once added, key in `ctrl+shift+p` (for windows) or `command+shift+p` (for mac) and find `Dev Containers: Reopen in Container`. This will run the whole project inside a container and install the following requirements:

1. **Docker**
2. **Serverless Framework**
3. **AWS CLI**

After the setup, run `serverless login` to log into your serverless account.

## Configuration

At the project root, the `serverless.containers.yml` file defines the SCF configuration:

```yaml
name: fastapi-example

deployment:
  type: awsApi@1.0

containers:
  app:
    src: ./app
    routing:
      pathPattern: /*
      pathHealthCheck: /health
    compute:
      type: awsFargateEcs # or awsLambda
      awsFargateEcs:
        cpu: 256
        memory: 512
```

This configuration sets:
- **Project Namespace:** The project name (fastapi-example) is used as a namespace in your AWS account.
- **Deployment Settings:** Configures networking (ALB, VPC, API Gateway) via the AWS API deployment type.
- **Container Details:**  
  - The source code is located in the `./app` directory.
  - A catch-all routing rule (`/*`) is used with a dedicated health check endpoint (`/health`).
  - The compute type is set to `awsFargateEcs`.

## Project Structure

Project structure for this FastAPI example:
```
fastapi-example/
├── .devcontainer/
│   └── devcontainer.json           # Dev Container configuration
├── app/
│   ├── Dockerfile                  # FastAPI Docker settings
│   ├── __init__.py
│   ├── main.py                     # Application entrypoint
│   ├── requirements.txt
│   └── static/                     # Static assets (css, images, etc.)
└── serverless.containers.yml
```

## Development

For local development, use Serverless Container Framework's development mode:
```bash
serverless dev
```

This will automatically start everything and set up hot reloading.

## Deployment

Deploy your FastAPI application to AWS by running:
```bash
serverless deploy
```

During deployment, SCF builds the container image (using the provided multi-stage Dockerfile) and provisions the necessary AWS resources (ALB, VPC, Lambda function or ECS Fargate service).

## Cleanup

To remove deployed AWS resources when they are no longer needed:
```bash
serverless remove --force --all
```

## Additional Resources

- [Serverless Container Framework Documentation](https://serverless.com/containers/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com)
- [AWS Lambda Documentation](https://aws.amazon.com/lambda)
- [AWS Fargate Documentation](https://aws.amazon.com/fargate) 