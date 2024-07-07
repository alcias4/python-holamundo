import sqlite3

# Nunca poner un string formatiado para evitar sql injection.

with sqlite3.connect("./app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?,?)",
        (1, "Hola mundo")
    )
