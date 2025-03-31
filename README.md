# FastAPI Application using Serverless Container Framework (SCF)

This example leverages the use of [Serverless Container Framework (SCF)](https://serverless.com/containers/docs) to build and deploy a basic FastAPI application in AWS Fargate (or AWS Lambda).

This application sets up a basic routing which includes a health check route and basic 404 response. Images and styles are copied from the official [Serverless Container Framework Repository](https://github.com/serverless/containers).

## Requirements

This project requires you to have an [AWS Account](https://console.aws.amazon.com/console/home) and [Serverless Account](https://app.serverless.com/).

If you are using VSCode or Cursor as your IDE, need to install [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

After cloning this repository, make sure that you set the following environment variables by running the following command:

```bash

export AWS_ACCESS_KEY_ID=               # your access key from aws
export AWS_SECRET_ACCESS_KEY=           # your secret key from aws
export AWS_REGION=                      # region you want to deploy the application
```

Once added, press `ctrl + shift + p` (for windows) or `command + shift + p` (for mac) and search for **"Dev Containers: Reopen in Container"**. This will setup the project in a containerized environment which includes the following programs:

1. **Docker** - [Documentation](https://docs.docker.com/)
2. **Serverless Framework** - [Documentation](https://www.serverless.com/framework/docs)
3. **AWS CLI** - [Documentation](https://docs.aws.amazon.com/cli/)

After the above process, open your integrated terminal and type `serverless login`. Choose **Login/Register** and it will then show a link, click the link and login to your Serverless account.

## The `serverless.containers.yml` config file

The `serverless.containers.yml` file defines the SCF configuration:

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
      type: awsFargateEcs # or awsLambda if you want to deploy it in AWS Lambda
      awsFargateEcs:
        cpu: 256
        memory: 512
```

Current configuration set details:
- **Project Namespace:** The project name (fastapi-example) will be used as namespace when it is deployed into your AWS account.
- **Deployment Settings:** This configures networking settings (ALB, VPC, API Gateway) via the AWS API deployment type.
- **Container Details:**  
  - The source code of the service is located in the `./app` directory.
  - A catch-all routing rule (`/*`) is used and a health check endpoint (`/health`).
  - The compute type is set to `awsFargateEcs`.

## Project Structure

Current Project Structure:
```
scf-fastapi-example/
├── .devcontainer/
│   └── devcontainer.json           # Configuration file for Dev Containers
├── app/
│   ├── Dockerfile                  # This is the FastAPI application image
│   ├── main.py                     # Holds the application itself together with routes
│   ├── requirements.txt
│   └── static/                     # Holds the images and styling (copied from the SCF Examples)
└── serverless.containers.yml       # Configuration file for SCF
```

## Development

For local development, use SCF's development mode:
```bash

serverless dev                # or `sls dev`
```

This will automatically start everything and set up hot reloading on your local environment. Default emulated ALB endpoint is pointing to `http://localhost:3000`.

## Deployment

Deploy your FastAPI application to AWS by running the following command:
```bash

serverless deploy               # or `sls deploy`
```

During deployment, SCF builds the docker image inside `app/` and provisions the necessary AWS resources (ALB, VPC, AWS Fargate service).

## Removing Resources

To remove your deployed AWS resources, run the following command:
```bash

serverless remove --force --all
```

## Additional Resources

- [Serverless Container Framework Documentation](https://serverless.com/containers/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com)
- [AWS Lambda Documentation](https://aws.amazon.com/lambda)
- [AWS Fargate Documentation](https://aws.amazon.com/fargate) 