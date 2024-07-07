import sqlite3

with sqlite3.connect("./app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "UPDATE usuarios SET nombre = ? WHERE id = ?",
        ("Jose Martinez", 1)
    )
