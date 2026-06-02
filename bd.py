import sqlite3 

conexion = sqlite3.connect("ciudadanos.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ciudadanos (
        dni TEXT,
        nombre TEXT,
        telefono TEXT,
        direccion TEXT,
        PRIMARY KEY (dni)
    )""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion)
    VALUES ('12345678', 'María García', '1122334455', 'Calle Falsa 123')""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion)
    VALUES ('12325676', 'María García', '1122334455', 'Calle Falsa 123')""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion)
        VALUES ('87654321', 'Juan Pérez', '9988776655', 'Av. Siempre Viva 742')""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion)
        VALUES ('11223344', 'Ana López', '3344556677', 'San Martín 456')""")

conexion.commit()
conexion.close()