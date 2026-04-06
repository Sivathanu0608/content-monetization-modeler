import mysql.connector
import pandas as pd


# ---------- CONNECT ----------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivathanu"
    )


# ---------- CREATE DATABASE ----------
def create_database():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS youtube_model")
    conn.close()


# ---------- CREATE TABLE ----------
def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivathanu",
        database="youtube_model"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        video_id VARCHAR(50),
        date DATE,
        views INT,
        likes INT,
        comments INT,
        watch_time_minutes FLOAT,
        video_length_minutes FLOAT,
        subscribers INT,
        category VARCHAR(50),
        device VARCHAR(50),
        country VARCHAR(50),
        ad_revenue_usd FLOAT
    )
    """)

    conn.close()


# ---------- LOAD CSV ----------
def load_csv(csv_path):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivathanu",
        database="youtube_model"
    )

    cursor = conn.cursor()

    # Load CSV
    df = pd.read_csv(csv_path)

    # Fix date column
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.date

    # Clear old data
    cursor.execute("DELETE FROM videos")

    # Insert data safely (fix NaN issue)
    for _, row in df.iterrows():
        clean_row = []

        for value in row:
            if pd.isna(value):
                clean_row.append(None)
            else:
                clean_row.append(value)

        cursor.execute("""
        INSERT INTO videos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(clean_row))

    conn.commit()
    conn.close()


# ---------- FETCH DATA ----------
def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sivathanu",
        database="youtube_model"
    )

    df = pd.read_sql("SELECT * FROM videos", conn)
    conn.close()
    return df