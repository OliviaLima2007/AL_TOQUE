import sqlite3

conexion = sqlite3.connect("turnos.bd")
cursor = conexion.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS turnos_disponibles(
        dni TEXT,
        tramite TEXT,
        fecha TEXT,
        hora TEXT,
        lugar TEXT,
        disponible TEXT
    )           
""")

cursor.execute(""" 
INSERT INTO turnos_disponibles (dni, tramite, fecha, hora, lugar, disponible)
    VALUES ('12345678', 'tramite', '15/07/2027', '09:00', 'municipalidad', 'si')
""")

conexion.commit()
conexion.close()