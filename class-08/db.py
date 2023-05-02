import sqlite3

mi_base = sqlite3.connect("electrodomesticos.db")

cursor = mi_base.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(40) NOT NULL,
                    stock INTEGER,
                    precio FLOAT NOT NULL,
                    descripcion VARCHAR(255)
                );""")

parametros = ('Licuadora', 5, 5900.90, 'Licuadora de 5 velocidades con baso de vidrio')
consulta = "INSERT INTO productos (nombre, stock, precio, descripcion) VALUES (?, ?, ?, ?)"
cursor.execute(consulta, parametros)
mi_base.commit()

parametros = (1,)
consulta = "SELECT * FROM productos"
cursor.execute(consulta)
datos = cursor.fetchall()
print(datos)

mi_base.close()  