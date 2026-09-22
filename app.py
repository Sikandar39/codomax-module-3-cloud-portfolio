import os
import json
import logging

from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import boto3
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv(
    "FLASK_SECRET_KEY",
    "change-this-in-production"
)

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET = os.getenv("S3_BUCKET")
SECRET_NAME = os.getenv("SECRET_NAME", "module3/database")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)


def get_database_secret():
    client = boto3.client(
        "secretsmanager",
        region_name=AWS_REGION
    )

    response = client.get_secret_value(
        SecretId=SECRET_NAME
    )

    return json.loads(response["SecretString"])


def get_db_connection():
    secret = get_database_secret()

    return psycopg2.connect(
        host=secret["host"],
        port=int(secret["port"]),
        database=secret["database"],
        user=secret["username"],
        password=secret["password"],
        connect_timeout=5
    )


def get_projects():
    connection = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, title, description, technology, category
            FROM projects
            ORDER BY id;
        """)

        projects = cursor.fetchall()

        cursor.close()

        return projects

    except Exception as error:
        logger.error(
            "Could not load projects: %s",
            error
        )

        return []

    finally:
        if connection:
            connection.close()


@app.route("/")
def home():

    projects = get_projects()

    return render_template(
        "index.html",
        projects=projects
    )


@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get(
        "name",
        ""
    ).strip()

    email = request.form.get(
        "email",
        ""
    ).strip()

    message = request.form.get(
        "message",
        ""
    ).strip()

    if not name or not email or not message:

        flash(
            "Please complete all contact fields."
        )

        return redirect(
            url_for("home") + "#contact"
        )

    connection = None

    try:

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO contact_messages
            (name, email, message)
            VALUES (%s, %s, %s)
            """,
            (
                name,
                email,
                message
            )
        )

        connection.commit()

        cursor.close()

        logger.info(
            "Contact message received from %s",
            email
        )

        flash(
            "Your message has been submitted successfully."
        )

    except Exception as error:

        logger.error(
            "Contact submission failed: %s",
            error
        )

        flash(
            "There was a problem submitting your message."
        )

    finally:

        if connection:
            connection.close()

    return redirect(
        url_for("home") + "#contact"
    )


@app.route("/download-cv")
def download_cv():

    try:

        s3 = boto3.client(
            "s3",
            region_name=AWS_REGION
        )

        response = s3.get_object(
            Bucket=S3_BUCKET,
            Key="Sikandar-Shah-CV.pdf"
        )

        logger.info(
            "CV downloaded from S3"
        )

        return send_file(
            response["Body"],
            mimetype="application/pdf",
            as_attachment=True,
            download_name="Sikandar-Shah-CV.pdf"
        )

    except Exception as error:

        logger.error(
            "S3 CV download failed: %s",
            error
        )

        return (
            "CV is currently unavailable.",
            404
        )


@app.route("/health")
def health():

    database_status = "offline"
    s3_status = "offline"

    try:

        connection = get_db_connection()

        connection.close()

        database_status = "online"

    except Exception as error:

        logger.error(
            "Database health check failed: %s",
            error
        )

    try:

        s3 = boto3.client(
            "s3",
            region_name=AWS_REGION
        )

        s3.head_bucket(
            Bucket=S3_BUCKET
        )

        s3_status = "online"

    except Exception as error:

        logger.error(
            "S3 health check failed: %s",
            error
        )

    return {
        "application": "online",
        "database": database_status,
        "s3": s3_status
    }


if __name__ == "__main__":

    logger.info(
        "Starting Sikandar Shah portfolio application"
    )

    app.run(
        host="127.0.0.1",
        port=5000
    )
