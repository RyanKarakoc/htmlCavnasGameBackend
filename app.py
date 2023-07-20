import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from models import *
from controller import *

load_dotenv()

app = Flask(__name__)

@app.route("/api/highscores", methods=["GET"])
def get_api_highscores():
    response = get_highscores()
    return response


@app.route("/api/highscore", methods=["GET"])
def get_api_highscore_query_username():
    response = get_highscore_query_username()
    return response


@app.route("/api/highscore", methods=["POST"])
def get_api_post_sumbit_score():
    response = post_sumbit_score()
    return response

