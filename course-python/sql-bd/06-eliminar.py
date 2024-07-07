import sqlite3

with sqlite3.connect("./app.db") as con:
    cursor = con.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (2,)
    )
