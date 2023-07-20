
from flask import request
from models import *

def get_highscores():
    data = fetch_all_highscores()
    return {"data": data}, 200

def get_highscore_query_username():
    username = request.args.get("username")
    data = fetch_highscore_by_username(username)
    return {"data": data}, 200

def post_sumbit_score():
    post_data = request.get_json()
    username = post_data["username"]
    score = post_data["score"]
    data = insert_highscore(username, score)
    return {"msg": data}, 201