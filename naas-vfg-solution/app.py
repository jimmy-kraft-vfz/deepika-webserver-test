# app.py
from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.environ.get("NAME", "Candidate")
    today = datetime.utcnow().strftime("%Y-%m-%d")
    return (
        "<html><head><meta charset='utf-8'><title>Hello</title></head>"
        "<body style='font-family:Helvetica,Arial,sans-serif; padding:2rem;'>"
        f"<h1>Hello DevOps NaaS {name} + {today}</h1></body></html>"
    )

@app.route("/health")
def health():
    return {"status": "ok", "date": datetime.utcnow().isoformat()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
