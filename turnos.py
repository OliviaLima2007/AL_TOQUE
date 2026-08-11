import tkinter as tk
import sqlite3
from conexion import buscar_ciudadano

#consulta a la base de datos de turnos
def buscar_turnos():
    conexion=sqlite3.connect("turnos.bd")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM turnos_disponibles")
    resultado=cursor.fetchall()
    conexion.close()
    return resultado

#llena los datos del turno
def abrir_turnos(ciudadanos):
    ventana = tk.Toplevel()
    ventana.title("AL TOQUE - TURNOS")
    ventana.state("zoomed")

    #encabezado
    encabezado = tk.Frame(ventana, bg="#145a32", pady=20)
    encabezado.pack(fill=tk.X)

    tk.Label(
        encabezado,
        text="AL TOQUE",
        font=("Arial",22,"bold"),
        bg="#145a32",
        fg="#a8f0c6"
    ).pack()

    tk.Label(
        encabezado,
        text="Tu tramite en tus manos.",
        font=("Arial",14,"italic"),
        bg="#145a32",
        fg="#d4f5e2"
    ).pack()

    #pie
    pie=tk.Frame(ventana, bg="#145a32", pady=10)
    pie.pack(fill=tk.X, side=tk.BOTTOM)
    
    tk.Label(
        pie,
        text="Sistema AL TOQUE | 2025")
        font=("Arial", 11)
        bg="#145a32",
        fg="#a8f0c6"
    ).pack()

    #cuerpo
    cuerpo=tk.Frame(ventana, bg="#1a3a2a")
    cuerpo.pack(expand=True, fill=tk.BOTH)
    
    tk.Label(cuerpo,
             text="SOLICITUD DE TURNO",
             font=("Arial",16,"bold")
             bg="#1a3a2a",
             fg="#ffffff").pack(pady=10)

    tk.Label(cuerpo,text=f"Nombre: {ciudadanos['nombre']}",font=("Arial", 16), bg="#1a3a2a", fg="#a8f0c6").pack()
    tk.Label(cuerpo,text=f"DNI: {ciudadanos['dni']}", font=("Arial", 16), bg="#1a3a2a", fg="#a8f0c6").pack()
    tk.Label(cuerpo,text=f"Teléfono: {ciudadanos['telefono']}", font=("Arial", 16), bg="#1a3a2a", fg="#a8f0c6").pack()
    tk.Label(cuerpo,text=f"Dirección: {ciudadanos['direccion']}", font=("Arial", 16), bg="#1a3a2a", fg="#a8f0c6").pack()
    tk.Label(cuerpo,text="SOLICITUD DE TURNO",font=("Arial",16,"bold"), font=("Arial", 16), bg="#1a3a2a", fg="#a8f0c6").pack()
    
    tk.Label(cuerpo, text="Trámite:", font=("Arial", 16), bg="#1a3a2a", fg="#d4f5e2").pack()
    entrada_tramite = tk.Entry(cuerpo, font=("Arial", 16), bg="#1a3a2a", fg="#d4f5e2")
    entrada_tramite.pack(pady=5)

    tk.Label(cuerpo, text="Fecha",  bg="#1a3a2a", fg="#d4f5e2")
    entrada_fecha =tk.Entry(cuerpo, font=("Arial", 16), bg="#1a3a2a", fg="#d4f5e2")
    entrada_fecha.pack(pady=5)

    tk.Label(cuerpo, text="Hora:",  bg="#1a3a2a", fg="#d4f5e2")
    entrada_hora =tk. Entry(cuerpo, font=("Arial", 16), bg="#1a3a2a", fg="#d4f5e2")
    entrada_hora.pack(pady=5)

    tk.Label(cuerpo, text="Lugar:", bg="#1a3a2a", fg="#d4f5e2")
    entrada_lugar = tk.Entry(cuerpo, font=("Arial", 16), bg="#1a3a2a", fg="#d4f5e2")
    entrada_lugar.pack(pady=5)

    tk.Label(cuerpo, text="Presione 1 para confirmar el turno", font=("Arial", 14), bg="#1a3a2a", fg="#6dbf8a").pack(pady=15)

    tk.Label(cuerpo,text="",justify="left",font=("Arial",13), bg="#1a3a2a", fg="#a8f0c6").pack(pady=10)

#guarda el turno
    def guardar():
            t = entrada_tramite.get()
            f = entrada_fecha.get()
            h = entrada_hora.get()
            l = entrada_lugar.get()
            comprobante.config(text=f"""
        TURNO REGISTRADO CORRECTAMENTE
        Ciudadano: {ciudadanos['nombre']}
        DNI: {ciudadanos['dni']}
        Teléfono: {ciudadanos['telefono']}
        Dirección: {ciudadanos['direccion']}
        Trámite: {t}
        Fecha: {f}
        Hora: {h}
        Lugar: {l} """)
        
    def on_key_Prees(event):
            if event.char=="1":
                    guardar()

    ventana.bind("<KeyPress>", on_key_Prees)
