import sqlite3


with sqlite3.connect("./app.db") as connection:

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )

# si no se usar el metodo de commit no se va a realizar los cambios
# connection.commit()

# cerrar la conexion
# connection.close()
