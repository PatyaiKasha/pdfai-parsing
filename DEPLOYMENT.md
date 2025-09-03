# Deployment Guide

This guide provides an overview of how to deploy the AI PDF Parser application to the internet for real-world testing with users. Deploying a full-stack application involves several components: the frontend, the backend, the database, and the message broker/cache.

There are two main approaches you can take: using a **Platform as a Service (PaaS)** for simplicity, or an **Infrastructure as a Service (IaaS)** for more control.

---

## Option 1: Simple Deployment with PaaS (e.g., Render, Heroku)

This is the recommended approach for getting started quickly. PaaS providers manage the underlying infrastructure, allowing you to focus on the code. [Render](https://render.com/) is a modern choice that works well for this stack.

### 1. Backend Deployment (on Render)

1.  **Create a new "Web Service"** on Render and connect it to your Git repository.
2.  **Environment**:
    -   Set the runtime to "Docker".
    -   Render will use the `backend/Dockerfile` to build your image.
3.  **Environment Variables**:
    -   Go to the "Environment" tab and add all the variables from your `.env` file (e.g., `DATABASE_URL`, `REDIS_URL`, `JWT_SECRET_KEY`, `OPENAI_API_KEY`).
    -   **Important**: Use strong, randomly generated secrets for production.
4.  **Start Command**: Render should automatically detect the `CMD` from your `Dockerfile`.

### 2. Frontend Deployment (on Vercel)

[Vercel](https://vercel.com/) is the company behind Next.js and provides the best-in-class platform for deploying Next.js applications.

1.  **Create a new "Project"** on Vercel and connect it to your Git repository.
2.  **Framework Preset**: Vercel will automatically detect that it's a Next.js project.
3.  **Root Directory**: Set the root directory to `frontend`.
4.  **Environment Variables**:
    -   Add `NEXT_PUBLIC_API_URL` and set its value to the public URL of your backend service on Render (e.g., `https://your-backend-name.onrender.com/api/v1`).

### 3. Database & Redis (on Render)

1.  **Create a "PostgreSQL" managed database** on Render. It will provide you with a connection URL. Use this URL for the `DATABASE_URL` environment variable in your backend service.
2.  **Create a "Redis" instance** on Render. It will also provide a connection URL. Use this for the `REDIS_URL` environment variable.

---

## Option 2: Advanced Deployment with IaaS (e.g., AWS, GCP, Azure)

This approach offers maximum flexibility and scalability but requires more DevOps knowledge. Here is a high-level overview using AWS as an example.

### 1. Containerize the Application

-   Build production-ready Docker images for the backend and frontend.
-   Push these images to a container registry like **Amazon ECR (Elastic Container Registry)**.

### 2. Deploy the Backend

-   **Service**: Use **AWS Fargate** or **Amazon ECS (Elastic Container Service)** to run your backend container without managing servers.
-   **Configuration**:
    -   Create a Task Definition for your backend service.
    -   Configure environment variables using **AWS Secrets Manager** or Parameter Store.
    -   Set up an **Application Load Balancer** to route traffic to your service and handle SSL termination.

### 3. Deploy the Frontend

-   **Vercel**: The recommended approach is still to use **Vercel** for the frontend, pointing the `NEXT_PUBLIC_API_URL` to your AWS load balancer's DNS name.
-   **AWS Amplify / S3 + CloudFront**: Alternatively, you can deploy the Next.js app to AWS. Amplify simplifies this, or you can manually configure an S3 bucket for hosting and a CloudFront distribution for global delivery and SSL.

### 4. Managed Services

-   **Database**: Use **Amazon RDS (Relational Database Service)** to run a managed PostgreSQL instance.
-   **Redis**: Use **Amazon ElastiCache** for a managed Redis instance.
-   **File Storage**: For real file uploads, use **Amazon S3**. You will need to configure the backend with an S3 bucket name, access key, and secret key, and update the `file_service.py` to upload files there.

---

## General Considerations for Production

-   **CORS**: Ensure your backend's `allow_origins` in `main.py` includes your production frontend URL.
-   **Secrets Management**: Never hardcode secrets. Use the environment variable management provided by your hosting platform.
-   **CI/CD**: Set up a CI/CD pipeline (e.g., using GitHub Actions) to automatically build, test, and deploy your application whenever you push changes to your main branch.
-   **Monitoring**: Use logging and monitoring services (e.g., AWS CloudWatch, Datadog, Sentry) to track application performance and errors.
