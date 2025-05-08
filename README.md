# WebAppProject

This is a simple web application built with Flask, Redis, and Docker, following DevOps principles. The app features a visit counter that is stored in Redis and a health check endpoint to ensure proper connection to Redis.

## Project Structure
├── .github/
│ └── workflows/
│ └── test.yml # GitHub Actions workflow file
├── app.py # Flask application code
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration for Flask app
├── docker-compose.yml # Docker Compose configuration
├── .gitignore # Files to be excluded from Git
└── README.md # Project documentation


## Setup and Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/WebAppProject.git
   cd WebAppProject

2. Docker-compose up --build

3. Access the web app by visiting http://localhost:8000 in your browser.
   Health check http://localhost:8000/health

   This repository includes a GitHub Actions workflow for testing the application. The workflow runs on every pull request to the main branch. It checks that the app starts properly and that the /health endpoint responds with a 200 status code.

## Technologies Used
Flask (Python)

Redis

Docker

Docker Compose

GitHub Actions  


This README provides all the necessary information on setting up, running, and testing the application. It also mentions the technologies used in the project. You can edit it with your actual GitHub username where required.

