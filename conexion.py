import sqlite3

def buscar_ciudadano(dni):
    conexion = sqlite3.connect("ciudadanos.db")
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM ciudadanos WHERE dni = ?", (dni,))
    resultado = cursor.fetchone()
    
    conexion.close()
    
    if resultado:
        return {
            "dni": resultado[0],
            "nombre": resultado[1],
            "telefono": resultado[2],
            "direccion": resultado[3],
            "multas": resultado[4],
            "imp_inmobiliario": resultado[5],
            "abl": resultado[6],
            "domiciliario": resultado[7]
        }
    else:
        return None