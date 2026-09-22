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
    VALUES (30112233, "Lucía Fernández", "11-4455-1122", "Av. San Martín 1234, Merlo", None, "Al día", "Al día", "Al día", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
    VALUES (28998877, "Martín Gómez", "11-5566-2233", "Belgrano 567, Merlo", "Estacionamiento indebido - $15.000", "Vencido (2 cuotas)", "Vencido (2 cuotas)", "Vencido (2 cuotas)", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (35667788, "Rocío Álvarez", "11-6677-3344", "Rivadavia 890, Libertad", None, "Al día", "Al día", "Al día", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (27554466, "Diego Torres", "11-7788-4455", "Mitre 234, Merlo", "Infracción de tránsito - $8.500", "Al día", "Al día", "Al día", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (38221199, "Camila Ruiz", "11-8899-5566", "Sarmiento 456, Parque San Martín", None, "Vencido (1 cuota)", "Vencido (1 cuota)", "Vencido (1 cuota)", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (26887766, "Sergio Benítez", "11-2233-6677", "Alsina 678, Merlo", None, "Al día", "Al día", "Al día", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (40556677, "Ayelén Cabrera", "11-3344-7788", "San Juan 901, San Antonio de Padua", "Ruidos molestos - $5.000", "Vencido (3 cuotas)", "Vencido (3 cuotas)", "Vencido (3 cuotas)", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (25443322, "Roberto Sosa", "11-4455-8899", "Moreno 345, Merlo", None, "Al día", "Al día", "Al día", None, None, None)""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (37778855, "Florencia Medina", "11-5566-9900", "Pueyrredón 123, Libertad", None, "Al día", "Al día", "Al día", "EXP-2026-00457", "Obra particular", "En trámite")""")

cursor.execute("""
    INSERT INTO ciudadanos (dni, nombre, telefono, direccion, multas, imp_inmobiliario, abl, domiciliario, exp_numero, exp_tramite, exp_estado)
        VALUES (29334411, "Nicolás Herrera", "11-6677-0011", "Yrigoyen 789, Merlo", "Estacionamiento indebido - $15.000", "Vencido (1 cuota)", "Vencido (1 cuota)", "Vencido (1 cuota)", None, None, None)""")
conexion.commit()
conexion.close()
