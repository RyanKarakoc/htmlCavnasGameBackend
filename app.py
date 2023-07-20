import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from sql_queries import *

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get("/api/highscores")
def highscores():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(all_highscores())
            data = cursor.fetchall()
    return {"data": data}

@app.get("/api/highscore")
def highscore_query_username():
    try:
        username = request.args.get("username")
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(highscore_by_username(username))
                data = cursor.fetchone()
                if data is None:
                    return {"error": "No highscore data found for this username"}
                return {"data": data}
    except psycopg2.Error as e:
        print("Error executing the PostgreSQL query:", e)
        return {"error": "Internal server error"}

  
@app.post("/api/highscore")
def sumbit_score():
    data = request.get_json()
    username = data["username"]
    score = data["score"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(highscore_by_username(username))
            highscore = cursor.fetchall()
            print(len(highscore))
            if len(highscore) == 0:
                cursor.execute(create_highscores_table())
                cursor.execute(insert_highscore(username, score))
                return {"username": username, "score": score, "message": f"highscore submitted for {username}"}, 201
            else:
                return {"error": "username already taken"}
