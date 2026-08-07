import tkinter as tk
from conexion import buscar_ciudadano

VentanaBienvenida = tk.Tk()
VentanaBienvenida.title("AL TOQUE")
VentanaBbienvenida.state("zoomed")
VentanaBbienvenida.configure(bg="#1a3a2a")

#INICIO DE ENCABEZADO
encabezado=tk.Frame(VentanaBienvenida, bg="#145a32", pady=20)
encabezado.pack(fill=tk.X)

tk.Label(
  encabezado,
  text="AL TOQUE",
  font=("Arial", 22, "bold"),
  bg="#145a32",
  fg="#a8f0c6").pack()

tk.Label(
  encabezado,
  text="Tu trámite, en tus manos.",
  font=("Arial", 14, "italic"),
  bg="#145a32",
  fg="#a8f0c6").pack()
# FIN DE ENCABEZADO
#--------------------
#INICIO DE CUERPO 

cuerpo=tk.frame(VentanaBienvenida, bg="#1a3a2a")
cuerpo.pack(expand=True)

tk.Label(
  cuerpo,
  text="¡Bienvenido!",
  font=("Arial", 48, "bold"),
    bg="#1a3a2a",
    fg="#ffffff"
).pack(pady=(40, 10))

tk.Label(
  cuerpo,
  text="¡Bienvenido!",
  font=("Arial", 22),
    bg="#1a3a2a",
    fg="#a8f0c6"
).pack(pady=(0, 30))

dni=tk.Entry(cuerpo,
    font=("Arial", 36),
    fg="#1a3a2a",
    bg="#a8f0c6",
    insertbackground="#1a3a2a",
    justify="center",
    width=14,
    relief="flat",
    bd=0)
dni.focus_set()
dni.pack()

tk.Label(
    cuerpo,
    text="Presione ENTER para continuar",
    font=("Arial", 16),
    bg="#1a3a2a",
    fg="#6dbf8a"
).pack(pady=20)

mensaje_error = tk.Label(
    cuerpo,
    text="",
    font=("Arial", 16),
    bg="#1a3a2a",
    fg="#ff6b6b"
)
mensaje_error.pack()
#FIN DE CUERPO
#-----------------
#INICIO DE PIE
pie = tk.Frame(VentanaBienvenida, bg="#145a32", pady=10)
pie.pack(fill=tk.X, side=tk.BOTTOM)

tk.Label(
    pie,
    text="Sistema AL TOQUE  |  Municipalidad de Merlo  |  2025",
    font=("Arial", 11),
    bg="#145a32",
    fg="#a8f0c6"
).pack()
# FIN DE PIE
#------------
# INICIO DE LOGICA
def parametros():  
  ciudadanos = buscar_ciudadano(dni.get())
  if len(dni.get())!=8:
    mensaje_error.config(text="⚠ Por favor ingresá exactamente 8 números, sin puntos ni comas")
    return False  
  mensaje_error.config(text="")
  return True

def AbrirPrincipal():
  print("AbrirPrincipal llamado")
  from principal import VentanaPrincipal
  ciudadanos = buscar_ciudadano(dni.get())
  print("ciudadanos:", ciudadanos)
  if ciudadanos:
    VentanaBienvenida.withdraw()    
    VentanaPrincipal(ciudadanos)    
  else:
      mensaje_error.config(text="⚠ DNI no encontrado en el sistema")

def key_press(event):
  if parametros():
    AbrirPrincipal()

dni.bind("<Return>", key_press)
VentanaBienvenida.bind("<Return>", key_press)
VentanaBienvenida.mainloop()
# FIN DE LOGICA
