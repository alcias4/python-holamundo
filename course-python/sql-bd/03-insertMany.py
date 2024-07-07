import sqlite3


with sqlite3.connect("./app.db") as con:
    cusror = con.cursor()
    usuarios = [
        (2, "chanchito feliz"),
        (3, "Camilo Andrade")
    ]
    cusror.executemany(
        "insert into usuarios values(?,?)",
        usuarios,
    )
