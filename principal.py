import tkinter as tk

from multas import VentanaMultas
from turnos import VentanaTurnos
from impuestos import VentanaImpuestos
from expedientes import VentanaExpedientes

VentanaPrincipal = tk.Tk()
VentanaPrincipal.title("VentanaPrincipal")

texto=tk.Label(VentanaPrincipal, text="Seleccione uno de los siguientes números para ingresar a:").pack()
texto=tk.Label(VentanaPrincipal, text="1. Para ingresar a Multas").pack()
texto=tk.Label(VentanaPrincipal, text="2. Para ingresar a Turnos").pack()
texto=tk.Label(VentanaPrincipal, text="3. Para ingresar a Impuestos").pack()
texto=tk.Label(VentanaPrincipal, text="4. Para ingresar a Expedientes").pack()

def AbrirVentana(event):
  match event.char:
  case "1":
    VentanaMultas()
  case "2":
    VentanaTurnos()
  case "3":
    VentanaImpuestos()
  case "4":
    VentanaExpedientes()

VentanaPrincipal.bind("<KeyPress>",AbrirVentana)

VentanaPrincipal.mainloop()
