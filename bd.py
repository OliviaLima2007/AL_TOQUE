import sqlite3 

conexion = sqlite3.connect("ciudadanos.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ciudadanos (
        dni TEXT,
        nombre TEXT,
        telefono TEXT,
        direccion TEXT,
        multas TEXT,
        imp_inmobiliario TEXT,
        abl TEXT,
        domiciliario TEXT,
        exp_numero TEXT,
        exp_tramite TEXT,
        exp_estado TEXT,
        PRIMARY KEY (dni)
    )""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
    VALUES ('12345678', 'María García', '1122334455', 'Calle Falsa 123', '1500.50', 'al día', 'al día', 'al día', '101', 'ABL', 'en proceso')""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
    VALUES ('12325676', 'María Lopez', '1122336655', 'Calle Falsa 456',  'al día', '8750.00', 'al día', 'al día', '202', 'impuestos', 'en revision')""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES ('87654321', 'Juan Pérez', '9988776655', 'Av. Siempre Viva 742',  'al día', 'al día', '4200.75', 'al día', '303', 'cobro de jubilacion', 'no iniciado')""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES ('11223344', 'Ana López', '3344556677', 'San Martín 456',  'al día', 'al día', 'al día', '3950.50', '404', 'domiciliario', 'finalizado')""")

conexion.commit()
conexion.close()
