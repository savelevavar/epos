import sqlite3


def sql_table(con):
    cursorObj.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()


con = sqlite3.connect('epos_bot.db')
cursorObj = con.cursor()
sql_table(con)