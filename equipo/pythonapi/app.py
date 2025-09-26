from flask import Flask, jsonify
import mysql.connector
import settings

app = Flask(__name__)

@app.route("/")
def root():
    return {"message": "API is running"}

@app.route("/hello")
def hello():
    return {"message": "Hello from Python API!"}

@app.route("/db-check")
def db_check():
    try:
        conn = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )
        conn.close()
        return jsonify({"db_status": "Connected"})
    except Exception as e:
        return jsonify({"db_status": "Error", "details": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

