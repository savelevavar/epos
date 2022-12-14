import sqlite3


conn = sqlite3.connect('C:/Users/ACER/PycharmProjects/eposbot/data.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()