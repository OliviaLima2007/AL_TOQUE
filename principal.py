import tkinter as tk

from multas import VentanaMultas
from turnos import abrir_turnos
from impuestos import VentanaImpuestos
from expedientes import VentanaExpedientes

def VentanaPrincipal (ciudadanos):
  ventana = tik.Toplevel()
  ventana.title("VentanaPrincipal")
  texto=tk.Label(ventana, text="Seleccione uno de los siguientes números para ingresar a:").pack()
  texto=tk.Label(ventana, text="1. Para ingresar a Multas").pack()
  texto=tk.Label(ventana, text="2. Para ingresar a Turnos").pack()
  texto=tk.Label(ventana, text="3. Para ingresar a Impuestos").pack()
  texto=tk.Label(ventana, text="4. Para ingresar a Expedientes").pack()

def AbrirVentana(event):
  match event.char:
  case "1":
    VentanaMultas(ciudadanos)
  case "2":
    VentanaTurnos(ciudadanos)
  case "3":
    VentanaImpuestos(ciudadanos)
  case "4":
    VentanaExpedientes(ciudadanos)

ventana.bind("<KeyPress>",AbrirVentana)
ventana.focus_set()
