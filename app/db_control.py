import sqlite3
from app import app
from flask import g


def add_new_question(question, ans1, ans2, correct):
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()

    try:
        cursor.execute(f"""INSERT INTO test
                      (question, ans1, ans2, correct) VALUES
                      {question, ans1, ans2, correct}""")
        connection.commit()
        msg = str('success')
    except Exception as err:
        connection.rollback()
        msg = str(err)
    finally:
        connection.close()
        return msg


def get_all_tests():
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * from test")

    return cursor.fetchall()


@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, "_database", None)

    if db:
        db.close()
