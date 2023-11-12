import sqlite3 as sq

db = sq.connect('users.db')
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tg_id INTEGER,"
                "region TEXT)")
    db.commit()


async def insert_user(user_id, data):
    reg = data['region']
    cur.execute("INSERT INTO users (tg_id, region) VALUES (?, ?)", (user_id, reg))
    db.commit()


async def get_if_user(user_id):
    user = cur.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if user:
        region = cur.execute("SELECT region FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
        return region
    else:
        return False




if __name__ == '__main__':
    pass
