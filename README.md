# AI PDF Parser

This project is a full-stack web application designed to parse PDF files, extract structured data, and classify documents using AI. It features a modern backend API built with FastAPI and a reactive frontend built with Next.js.

## ✨ Features

-   **AI-Powered PDF Parsing**: Extract structured data, not just text.
-   **User Authentication**: Secure user registration and login with JWT.
-   **Asynchronous Processing**: PDF parsing is handled in the background by Celery workers, ensuring the UI remains responsive.
-   **Job History**: Users can view the status and results of their past jobs.
-   **Usage Tracking**: A simple plan and usage limit system.
-   **Dockerized Environment**: The entire stack can be run easily with Docker Compose.

## 🛠️ Tech Stack

-   **Backend**: FastAPI, Python 3.11, PostgreSQL, Redis, Celery
-   **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS, Zustand
-   **DevOps**: Docker, Docker Compose

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

You must have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your system.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Configure Environment Variables

The project uses environment variables for configuration. A template is provided in `.env.example`.

1.  **Create a `.env` file:**
    ```bash
    cp .env.example .env
    ```

2.  **Edit the `.env` file:**
    Open the newly created `.env` file in a text editor. For local development, the default values are sufficient. However, you should **change `JWT_SECRET_KEY`** to a long, random string for security. You will also need to add your own `OPENAI_API_KEY`.

### 3. Build and Run the Application

With Docker and Docker Compose installed, you can build and run the entire application stack with a single command:

```bash
docker-compose -f docker-compose.dev.yml up --build
```

-   `--build`: This flag tells Docker Compose to build the images for the backend and frontend before starting the containers. You only need to use it the first time or when you make changes to the `Dockerfile`s or dependencies.
-   It may take a few minutes to download the base images and build the services the first time you run this command.

Once the services are running, you can access them at:

-   **Frontend Application**: [http://localhost:3000](http://localhost:3000)
-   **Backend API Docs (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧪 Manual Testing Guide

Here’s a simple workflow to test the core functionality of the application:

1.  **Navigate to the Frontend**: Open your web browser and go to [http://localhost:3000](http://localhost:3000).

2.  **Register a New User**:
    -   Click on "Get started" or the "Register" link.
    -   On the registration page, enter a valid email address and a password (must be at least 8 characters).
    -   Click "Create Account". You should be automatically logged in and redirected to the dashboard.

3.  **Explore the Dashboard**:
    -   You should see a welcome message.
    -   Check the navigation links on the left for Upload, History, etc.

4.  **Upload a PDF**:
    -   Navigate to the "Upload" page.
    -   Drag and drop a PDF file onto the upload area, or click "Or choose a file" to select one.
    -   Upon successful upload, you will be redirected to the "History" page.

5.  **Check Job Status**:
    -   On the "History" page, you should see your new job listed with a "pending" or "processing" status.
    -   The status badge for "processing" will have a pulsing animation.
    -   Wait for about 15-30 seconds for the background worker to simulate the processing.
    -   Refresh the page. The job status should update to "completed" or "failed".

6.  **Log Out and Log In**:
    -   (Note: A logout button is not yet implemented in the UI, but the underlying state management is in place).
    -   You can test logging out by clearing your browser's local storage for `localhost:3000` and refreshing the page.
    -   Go to the login page, enter your credentials, and verify that you can log back in successfully.

## 🛑 Stopping the Application

To stop all running containers, press `Ctrl+C` in the terminal where `docker-compose` is running. To remove the containers and the network, run:

```bash
docker-compose -f docker-compose.dev.yml down
```

To also remove the database volume (deleting all data), run:
```bash
docker-compose -f docker-compose.dev.yml down -v
```
