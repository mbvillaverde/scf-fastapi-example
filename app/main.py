import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return HTMLResponse(
        f"""
        <html>
        <head>
            <title>Serverless Container Framework</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
            <link rel="icon" type="image/png" href="/static/images/favicon.png">
        </head>
        <body>
            <div class="container">
            <img src="/static/images/logo.png" alt="Logo" class="logo">
            <div class="info">Namespace: {os.getenv("SERVERLESS_NAMESPACE")}</div>
            <div class="info">Container Name: {os.getenv("SERVERLESS_CONTAINER_NAME")}</div>
            <div class="info">Stage: {os.getenv("SERVERLESS_STAGE")}</div>
            <div class="info">Compute Type: {os.getenv("SERVERLESS_COMPUTE_TYPE")}</div>
            <div class="info">Local: {os.getenv("SERVERLESS_LOCAL")}</div>
            </div>
        </body>
        </html>
        """
    )


@app.get("/health")
def health_check():
    return {"message": "OK"}


@app.exception_handler(404)
def handle_404(_: Request, exception: Exception):
    return HTMLResponse(
        """
        <html>
        <head>
            <title>404 - Page Not Found</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
            <link rel="icon" type="image/png" href="/static/images/favicon.png">
        </head>
        <body>
            <div class="container">
            <h1>404 - Page Not Found</h1>
            <a href="/">Return to Home</a>
            </div>
        </body>
        </html>
        """,
        status_code=exception.status_code,
    )
