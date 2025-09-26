Project structure : 

naas-devops-webapp/
├── Dockerfile         # Docker build file
└── app/
    └── index.html     # Web page served by Nginx

Prerequisites :

<B>Docker</B> :
 installed on your system.

A Docker Hub account (https://github.com/)

Build the Docker Image 

Command :  docker build -t naas-devops-webapp:latest .

SIT env : docker build -t naas-devops-webapp:sit .
UAT env : docker build -t naas-devops-webapp:uat .
Run the Container

command : docker run -d -p 8080:80 --name naas-devops-webapp naas-devops-webapp:latest (Start the container and map port 8080)

Open browser and go to:

http://localhost:8080

