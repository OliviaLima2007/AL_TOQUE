import tinker as tk

VentanaBienvenida = tk.Tk()
VentanaBienvenida.title("VentanaBienvenida")

texto=tk.Label(VentanaBienvenida, text="!Bienvenida¡, Ingrese su DNI")
texto.pack()

dni=tk.Entry(VentanaBienvenida)
dni.config(fg="white", bg="black", font=("arial",12))
dni.pack()

texto=tk.Label(VentanaBienvenida, text="Para continuar por favor apretar ENTER")
texto.pack()

def parametros():
  numero=int(dni.get())
  if len(numero)!=8:
    texto=tk.Label(VentanaBienvenida, text="Por favor ingresar 8 numeros, sin puntos ni comas")
    texto.pack()
    return False
    return True

def AbrirPrincipal():
  from principal import VentanaPrincipal
  VentanaPrincipal()

def key_press(event):
  if parametros():
    AbrirPrincipal()

VentanaPrincipal.bind("<Return>", key_press)

VentanaPrincipal.mainloop()
