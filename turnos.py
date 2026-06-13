import tkinter as tk
import sqlite3
from conexion import buscar_ciudadano

ventana = tk.Toplevel()

def buscar_turnos():
    conexion=aqlite3.connect("turnos.bd")
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM turnos_disponibles")
    resultado=cursor.fetchall()
    conexion.close()
    return resultado

def abrir_turnos(ciudadano):
        ventana.title("Turnos")
        ventana.geometry("600x600")
datos=tk.Label(ventana,text="DATOS DEL CIUDADANO",font=("Arial",16,"bold"))
datos.pack(pady=10)
nombre=tk.Label(ventana,text=f"Nombre: {ciudadano['nombre']}")
nombre.pack()
dni=tk.Label(ventana,text=f"DNI: {ciudadano['dni']}")
dni.pack()
telefono=tk.Label(ventana,text=f"Teléfono: {ciudadano['telefono']}")
telefono.pack()
direccion=tk.Label(ventana,text=f"Dirección: {ciudadano['direccion']}")
direccion.pack()
 #   Label(ventana, text="").pack()

solicitud=tk.Label(ventana,text="SOLICITUD DE TURNO",font=("Arial",16,"bold"))
solicitud.pack(pady=10)

tramite=tk.Label(ventana, text="Trámite")
tramite.pack()

entrada_tramite = tk.Entry(ventana)
entrada_tramite.pack()

fecha=tk.Label(ventana, text="Fecha").pack()

entrada_fecha =tk.Entry(ventana)
entrada_fecha.pack()

hora=tk.Label(ventana, text="Hora").pack()

entrada_hora =tk. Entry(ventana)
entrada_hora.pack()

lugar=tk.Label(ventana, text="Lugar").pack()

entrada_lugar = tk.Entry(ventana)
entrada_lugar.pack()

comprobante = tk.Label(ventana,text="",justify=LEFT,font=("Arial",11))

comprobante.pack(pady=20)

def guardar():

        tramite = entrada_tramite.get()
        fecha = entrada_fecha.get()
        hora = entrada_hora.get()
        lugar = entrada_lugar.get()

        crear_turno(
            ciudadano,
            tramite,
            fecha,
            hora
        )

        comprobante.config(
            text=f"""
TURNO REGISTRADO CORRECTAMENTE

Ciudadano: {ciudadano['nombre']}
DNI: {ciudadano['dni']}
Teléfono: {ciudadano['telefono']}
Dirección: {ciudadano['direccion']}

Trámite: {tramite}
Fecha: {fecha}
Hora: {hora}
Lugar: {lugar}
"""
        )

        mostrar_turnos()

def on_key_Prees(event):
      if event.char=="1":
        guardar()

ventana.bind("<KeyPress>", on_key_Prees)

ventana.mainloop()
