import sqlite3

def create_database():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(username, password, role):

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username,password,role) VALUES(?,?,?)",
            (username, password, role)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login_user(username, password):

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user