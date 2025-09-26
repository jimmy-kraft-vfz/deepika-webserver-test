# Dockerfile
FROM python:3.11-slim

WORKDIR /app

#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies directly
RUN pip install --no-cache-dir Flask==2.3.2 pytest==7.4.0 requests==2.31.0

COPY app.py .

# create non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8080
ENV NAME="  "

CMD ["python", "app.py"]
