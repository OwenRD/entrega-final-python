import sqlite3

conexion = sqlite3.connect("productosord.db")
cursor = conexion.cursor()
print("database se Ejecuto")

def crear_tabla():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        descripcion TEXT,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL
    )
    """)

    conexion.commit()

def cerrar_conexion():

    conexion.close()