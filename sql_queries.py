def create_highscores_table():
    return ("CREATE TABLE IF NOT EXISTS highscores (id SERIAL PRIMARY KEY, username TEXT, score INT);")


def insert_highscore(username, score):
    return f"INSERT INTO highscores (username, score) VALUES ('{username}', {score}) RETURNING id;"


def all_highscores():
    return "SELECT * FROM highscores ORDER BY score DESC"

def highscore_by_username(username):
    return f"SELECT * FROM highscores WHERE username='{username}';"