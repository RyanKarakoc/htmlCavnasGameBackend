from dotenv import load_dotenv
from flask import Flask
from models import *
from controller import *
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

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

if __name__ == "__main__":
    app.run()