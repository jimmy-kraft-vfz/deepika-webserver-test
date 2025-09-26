# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# create non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8080
ENV NAME="  "

CMD ["python", "app.py"]
