import tkinter as tk

ventana =tk.Toplevel()

# ---------------- IMPUESTOS ---------------- #
#menu principal
def impuestos():    
    ventana.title("Impuestos y Pagos")
    ventana.geometry("400x300")

    lbl = tk.Label(ventana,
        text="Seleccione una opción",
        font=("Arial", 12, "bold"))
    lbl.pack(pady=10)

    lbl = tk.Label(ventana, text="Presione 1 para pagar impuesto inmobiliario")
    lbl.pack(pady=5)

    lbl = tk.Label(ventana, text="Presione 2 para pagar patente auto/moto")
    lbl.pack(pady=5)

    lbl = tk.Label(ventana, text="Presione 3 para pagar ABL")
    lbl.pack(pady=5)        

    lbl = tk.Label(ventana, text="Presione 4 para Consultar deuda total")
    lbl.pack(pady=5)        

def key_press(event):
    match event.char:
        case "1":
          abrir_pagos("Inmobiliario", ciudadanos['imp_inmobiliario'])
        case "2":
          abrir_pagos("ABL", ciudadanos['patente'])
        case "3":
          abrir_pagos("ABL", ciudadanos['abl'])
        case "4":
          abrir_pagos("Domiciliario", ciudadanos['domiciliario'])

def abrir_pagos(impuesto, monto):
    ventana_pagos = tk.Toplevel()
    ventana_pagos.title("Pagos")
    ventana_pagos.geometry("400x350")

    lbl = tk.Label(ventana_pagos, text=f"Impuesto: {impuesto}")
    lbl.pack(pady=10)
    lbl = tk.Label(ventana_pagos, text=f"Monto: ${monto}")
    lbl.pack(pady=5)
    lbl = tk.Label(ventana_pagos, text="Presione 1 para pagar | 2 cancelar")
    lbl.pack(pady=10)

    resultado = tk.Label(ventana_pagos, text="")
    resultado.pack(pady=10)

def abrir_pagos(impuesto, monto):
    ventana_confirmacion = tk.Toplevel()
    ventana_confirmacion.title("Confirmación")
    ventana_confirmacion.geometry("400x250")

    tk.Label(ventana_confirmacion, text=f"Impuesto: {impuesto}").pack(pady=10)
    tk.Label(ventana_confirmacion, text=f"Monto: ${monto}").pack(pady=5)
    tk.Label(ventana_confirmacion, text="Presione 1 para pagar | 2 para cancelar").pack(pady=10)

    resultado = tk.Label(ventana_confirmacion, text="")
    resultado.pack(pady=10)

    def on_key_Press(event):
        match event.char:
            case "1":
                ventana_confirmacion.destroy()
                metodo_pago()
            case "2":
                resultado.config(text="Operación cancelada")

    ventana_confirmacion.bind("<KeyPress>", on_key_Press)
    ventana_confirmacion.focus_set()

def metodo_pago():
    ventana_pago = tk.Toplevel()
    ventana_pago.title("Método de pago")
    ventana_pago.geometry("400x250")

    tk.Label(ventana_pago, text="1. Pagar con Tarjeta").pack(pady=10)
    tk.Label(ventana_pago, text="2. Pagar con QR").pack(pady=5)
    tk.Label(ventana_pago, text="3. Cancelar").pack(pady=5)

    resultado = tk.Label(ventana_pago, text="")
    resultado.pack(pady=10)

    def on_key_Press(event):
        match event.char:
            case "1":
                resultado.config(text="Pago con Tarjeta realizado. Imprimiendo ticket...")
            case "2":
                resultado.config(text="Pago con QR realizado. Imprimiendo ticket...")
            case "3":
                ventana_pago.destroy()

    ventana_pago.bind("<KeyPress>", on_key_Press)
    ventana_pago.focus_set()

# ---------------- MULTAS ---------------- #

def multas():
    ventana.title("Multas")
    ventana.geometry("400x300")

    lbl = tk.Label(ventana,
    text="Multas",
    font=("Arial", 14, "bold"))
    lbl.pack(pady=10)

    lbl = tk.Label(ventana, text="presione 1 para consultar multas de tránsito")
    lbl.pack(pady=10)

    lbl = tk.Label(ventana,
            text="Presione 2 para pagar multas de tránsito")
    lbl.pack(pady=10)

def on_key_Press(event):
        match event.char:
            case "1":
                abrir_consulta()
            case "2":
                abrir_pago()
            

def abrir_consulta():
    lbl = tk.Label(ventana, text=f"Multas: {ciudadanos['multas']}")
    lbl.pack(pady=10)


def abrir_pago():
    ventana_pago = tk.Toplevel()
    ventana_pago.title("Pago de Multas")
    ventana_pago.geometry("400x250")

    lbl = tk.Label(ventana_pago, text="1. Pagar con Tarjeta").pack(pady=5)
    lbl = tk.Label(ventana_pago, text="2. Pagar con QR")
    lbl = tk.Label(ventana_pago, text="3. Cancelar").pack(pady=5)
    lbl.pack(pady=5)

    resultado = tk.Label(ventana_pago, text="")
    resultado.pack(pady=10)

    def on_key_Press(event):
        match event.char:
            case "1":
                resultado.config(text="Pago con Tarjeta realizado. Imprimiendo ticket...")
            case "2":
                resultado.config(text="Pago con QR realizado. Imprimiendo ticket...")
            case "3":
                ventana_pago.destroy()

    ventana_pago.bind("<KeyPress>", on_key_Press)
    ventana_pago.focus_set()
