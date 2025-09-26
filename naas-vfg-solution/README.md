# Candidate Webserver Test(Deepika Gupta)

Simple Flask webserver that displays "Hello DevOps NaaS &lt;NAME&gt; + &lt;DATE&gt;".

<B>Project structure</B> : 

```
naas-vfg-solution/
├── Dockerfile # Docker build file
├── app.py # Main application
├── test_app.py # Test script
├── requirements.txt # Python dependencies
└── docker-compose.yml # Docker Compose config
```
    
<B>Prerequisites</B> :

Docker :
 installed on your system.

<B>A Docker Hub account</B> (https://github.com/)

<B>Build the Docker Image </B>

Command :  

## Local
docker build -t deepika-webserver-test:local .
## sit
docker build -t deepika-webserver-test:sit .
##uat
docker build -t deepika-webserver-test:uat .


Run the Container

docker run -d -p 8080:80 --name naas-devops-webserver <deepika-Webserver-Test>:latest

<B>Open browser and go to:</B>

http://127.0.0.1:8080


