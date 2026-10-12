from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)

# Exposes application metrics at /metrics for Prometheus.
metrics = PrometheusMetrics(app)
metrics.info("app_info", "DevOps Demo Application", version="1.0.0")


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Demo App",
        "status": "running",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "message": "End-to-end DevOps pipeline is working!"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
