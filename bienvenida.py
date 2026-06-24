import tkinter as tk
from conexion import buscar_ciudadano

VentanaBienvenida = tk.Tk()
VentanaBienvenida.title("VentanaBienvenida")

texto=tk.Label(VentanaBienvenida, text="!Bienvenida¡, Ingrese su DNI")
texto.pack()

dni=tk.Entry(VentanaBienvenida)
dni.focus_set()
dni.config(fg="white", bg="black", font=("arial",12))
dni.pack()

texto=tk.Label(VentanaBienvenida, text="Para continuar por favor apretar ENTER")
texto.pack()

def parametros():  
  ciudadanos = buscar_ciudadano(dni.get())
  if len(dni)!=8:
    texto=tk.Label(VentanaBienvenida, text="Por favor ingresar 8 numeros, sin puntos ni comas").pack()
    return False
  return True

def AbrirPrincipal():
  from principal import VentanaPrincipal
  ciudadanos = buscar_ciudadano(dni.get())
  if ciudadanos:
    VentanaPrincipal(ciudadanos)
    VentanaBienvenida.withdraw()    
  else:
      tk.label(VentanaBienvenida,text="DNI no encontrado").pack()

def key_press(event):
  if parametros():
    AbrirPrincipal()

VentanaBienvenida.bind("<Return>", key_press)

VentanaBienvenida.mainloop()
