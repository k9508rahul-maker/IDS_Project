from flask import Flask, render_template, request
import joblib
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Load trained model
model = joblib.load("model/ids_model.pkl")
encoder = joblib.load("model/label_encoder.pkl")

DATABASE = "ids.db"


# -----------------------------
# Database
# -----------------------------
def init_db():
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            packet_size INTEGER,
            connection_count INTEGER,
            failed_connections INTEGER,
            duration INTEGER,
            result TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Dashboard
# -----------------------------
@app.route("/")
def dashboard():

    conn = sqlite3.connect(DATABASE)

    total = conn.execute(
        "SELECT COUNT(*) FROM alerts"
    ).fetchone()[0]

    attacks = conn.execute(
        "SELECT COUNT(*) FROM alerts WHERE result='Attack'"
    ).fetchone()[0]

    normal = conn.execute(
        "SELECT COUNT(*) FROM alerts WHERE result='Normal'"
    ).fetchone()[0]

    recent_alerts = conn.execute("""
        SELECT *
        FROM alerts
        ORDER BY id DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        attacks=attacks,
        normal=normal,
        alerts=recent_alerts
    )


# -----------------------------
# Prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    packet_size = int(request.form["packet_size"])
    connection_count = int(request.form["connection_count"])
    failed_connections = int(request.form["failed_connections"])
    duration = int(request.form["duration"])

    features = [[
        packet_size,
        connection_count,
        failed_connections,
        duration
    ]]

    prediction = model.predict(features)[0]

    result = encoder.inverse_transform([prediction])[0]

    # Save result
    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        INSERT INTO alerts
        (
            packet_size,
            connection_count,
            failed_connections,
            duration,
            result,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        packet_size,
        connection_count,
        failed_connections,
        duration,
        result,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        result=result,
        packet_size=packet_size,
        connection_count=connection_count,
        failed_connections=failed_connections,
        duration=duration
    )


# -----------------------------
# Start application
# -----------------------------
if __name__ == "__main__":
    init_db()

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )