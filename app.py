from flask import Flask
import redis
import os

app = Flask(__name__)

# Load Redis connection info from environment variables
redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))

# Connect to Redis
try:
    r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
    r.ping()
except redis.ConnectionError:
    r = None


@app.route("/")
def home():
    return "Welcome to my DevOps app!"


@app.route("/visit")
def visit():
    if r:
        count = r.incr("visits")
        return f"Visit count: {count}"
    return "Redis not available", 500


@app.route("/health")
def health():
    if r:
        try:
            r.ping()
            return "OK", 200
        except redis.ConnectionError:
            pass
    return "Redis connection failed", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
