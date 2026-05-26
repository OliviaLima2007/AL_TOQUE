import tinker as tk

VentanaBienvenida = tk.Tk()
VentanaBienvenida.title("VentanaBienvenida")

texto=tk.Label(VentanaBienvenida, text="!Bienvenida¡, Ingrese su DNI")
texto.pack()

dni=tk.Entry(VentanaBienvenida)
dni.config(fg="white", bg="black", font=("arial",12))
dni.pack()
