from connection import connection

def create_highscores_table():
    return ("CREATE TABLE IF NOT EXISTS highscores (id SERIAL PRIMARY KEY, username TEXT, score INT);")

def fetch_all_highscores():
    query_string = "SELECT username, score FROM highscores ORDER BY score DESC;"
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query_string)
            data = cursor.fetchall()
    return data

def fetch_highscore_by_username(username):
    query_string = f"SELECT * FROM highscores WHERE username='{username}';"
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query_string)
            data = cursor.fetchone()
            if data is None:
                return {"msg": "No highscore data found for this username"}
            return data
        
def insert_highscore(username, score):
    query_string = f"INSERT INTO highscores (username, score) VALUES ('{username}', {score}) RETURNING *;"
    check_user = fetch_highscore_by_username(username)
    print(type(check_user))
    if type(check_user) is dict:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query_string)
                data = cursor.fetchall()
                return data
    else:
        return {"error": "username already taken"}
