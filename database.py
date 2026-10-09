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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        study REAL,
        attendance REAL,
        previous_marks REAL,
        assignments REAL,
        sleep REAL,
        predicted_score REAL
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
    except sqlite3.IntegrityError:
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


def save_prediction(name, study, attendance, previous_marks,
                    assignments, sleep, predicted_score):

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (name, study, attendance, previous_marks, assignments, sleep, predicted_score)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        study,
        attendance,
        previous_marks,
        assignments,
        sleep,
        predicted_score
    ))

    conn.commit()
    conn.close()


def get_predictions():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")

    data = cursor.fetchall()

    conn.close()
    return data


def clear_predictions():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM predictions")

    conn.commit()
    conn.close()


create_database()