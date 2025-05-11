## WebAppProject

This is a simple web application built with Flask, Redis, and Docker, following DevOps principles. The app features a visit counter that is stored in Redis and a health check endpoint to ensure proper connection to Redis.

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── test.yml
└── README.md

```


## Setup Instructions and Run Locally

###1. Clone the repository:

   ```bash
   git clone https://github.com/GeorgiGabrilov/WebAppProject.git
   cd WebAppProject
   ```
   
###2. Build and run container

    
    docker-compose up --build
    

###3. Access the web app 
    ```
    visit http://localhost:8000 in your browser.
    Health check http://localhost:8000/health

   This repository includes a GitHub Actions workflow for testing the application , the workflow runs on every pull request to the main branch. It checks that the app starts properly and that the /health endpoint responds with a 200 status code.
    ```

### Technologies Used
Flask (Python)

Redis

Docker

Docker Compose

GitHub Actions  


This README provides all the necessary information on setting up, running, and testing the application. It also mentions the technologies used in the project. You can edit it with your actual GitHub username where required.

