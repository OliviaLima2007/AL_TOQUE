import tkinter as tk

from Multas import VentanaMultas
from turnos import abrir_turnos
from impuestos import VentanaImpuestos
from expedientes import VentanaExpedientes

def VentanaPrincipal (ciudadanos):
  ventana = tk.Toplevel()
  ventana.state("zoomed")
  ventana.title("AL TOQUE")

  #encabezado
  encabezado = tk.Frame(ventana, bg="#145a32", pady=20)
  encabezado.pack(fill=tk.X)

  tk.Label(
      encabezado,
      text="MUNICIPALIDAD DE MERLO",
      font=("Arial", 22, "bold"),
      bg="#145a32",
      fg="#a8f0c6"
    ).pack()

  tk.Label(
      encabezado,
      text="Tu trámite, en tus manos.",
      font=("Arial", 14, "italic"),
      bg="#145a32",
      fg="#d4f5e2"
    ).pack()

  #pie
    pie = tk.Frame(ventana, bg="#145a32", pady=10)
  pie.pack(fill=tk.X, side=tk.BOTTOM)

  tk.Label(
        pie,
        text="Sistema AL TOQUE | 2025",
        font=("Arial", 11),
        bg="#145a32",
        fg="#a8f0c6"
    ).pack()

#cuerpo
  cuerpo=tk.Frame(ventana, bg="#1a3a2a")
  cuerpo.pack(expand=True, fill=tk.BOTH)

  tk.Label(
    cuerpo,
    text=f"Bienvenido/a, {ciudadanos['nombre']}",
    font=("Arial", 32, "bold"),
    bg="#1a3a2a",
    fg="#ffffff"    
  ).pack(pady=(40,20))

tk.Label(
    cuerpo,
    text="Seleccione una opción:",
    font=("Arial", 20),
    bg="#1a3a2a",
    fg="#a8f0c6"  
  ).pack(pady=(0,30))

opciones=[
  "1 🠮 Multas",
  "2 🠮 Turnos",
  "3 🠮 Impuestos",
  "4 🠮 Expedientes",
  "5 🠮 Salir",
  ]

  for opcion in opciones:
    tk.Label(
      cuerpo,
      text=opcion,
      font=("Arial", 22),
      bg="#1a3a2a",
      fg="#a8f0c6",
      anchor="w",
      width=30
    )pack(pady=8)
    
  def AbrirVentana(event):
      match event.char:
        case "1":
          turnos_tramites(ciudadanos)
        case "2":
          abrir_turnos(ciudadanos)
        case "3":
          VentanaImpuestos(ciudadanos)
        case "4":
          VentanaExpedientes(ciudadanos)
        case "5":
           ventana.destroy()

  ventana.bind("<KeyPress>",AbrirVentana)
  ventana.focus_set()
