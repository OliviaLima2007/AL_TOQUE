import tkinter as tk
import sqlite3
from conexion import buscar_ciudadano

ventana = tk.Toplevel()
#consulta a la base de datos de turnos
def buscar_turnos():
    conexion=aqlite3.connect("turnos.bd")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM turnos_disponibles")
    resultado=cursor.fetchall()
    conexion.close()
    return resultado

#llena los datos del turno
def abrir_turnos(ciudadanos):
    ventana.title("Turnos")
    ventana.geometry("600x600")
    datos=tk.Label(ventana,text="DATOS DEL CIUDADANO",font=("Arial",16,"bold")).pack(pady=10)
    nombre=tk.Label(ventana,text=f"Nombre: {ciudadanos['nombre']}").pack()
    dni=tk.Label(ventana,text=f"DNI: {ciudadanos['dni']}").pack()
    telefono=tk.Label(ventana,text=f"Teléfono: {ciudadanos['telefono']}").pack()
    direccion=tk.Label(ventana,text=f"Dirección: {ciudadanos['direccion']}").pack()
    solicitud=tk.Label(ventana,text="SOLICITUD DE TURNO",font=("Arial",16,"bold")).pack(pady=10)
    tramite=tk.Label(ventana, text="Trámite").pack()        
    entrada_tramite = tk.Entry(ventana).pack()        
    fecha=tk.Label(ventana, text="Fecha").pack()        
    entrada_fecha =tk.Entry(ventana).pack()        
    hora=tk.Label(ventana, text="Hora").pack()        
    entrada_hora =tk. Entry(ventana).pack()        
    lugar=tk.Label(ventana, text="Lugar").pack()        
    entrada_lugar = tk.Entry(ventana).pack()        
    comprobante = tk.Label(ventana,text="",justify=LEFT,font=("Arial",11)).pack(pady=20)

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
