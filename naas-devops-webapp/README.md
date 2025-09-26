<B>Project structure</B> : 

```
naas-devops-webapp/
├── Dockerfile         # Docker build file
└── app/
    └── index.html     # Web page served by Nginx
```
<B>Prerequisites</B> :

Docker :
 installed on your  system.

<B>A Docker Hub account</B> (https://github.com/)

<B>Build the Docker Image</B>

Command :  <B> docker build -t naas-devops-webapp:latest . </B>

<B>SIT env : docker build -t naas-devops-webapp:sit .</B>

<B>UAT env : docker build -t naas-devops-webapp:uat . </B>

Run the Container

command : docker run -d -p 8080:80 --name naas-devops-webapp naas-devops-webapp:latest (Start the container and map port 8080)

<B>Open browser and go to:</B>

http://localhost:8080

