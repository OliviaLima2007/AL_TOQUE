import tkinter as tk

def VentanaImpuestos(ciudadano):
    ventana = tk.Toplevel()
    ventana.title("AL TOQUE - Impuestos")
    ventana.state("zoomed")
    ventana.configure(bg="#1a3a2a")

    # ENCABEZADO
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

    # PIE
    pie = tk.Frame(ventana, bg="#145a32", pady=10)
    pie.pack(fill=tk.X, side=tk.BOTTOM)

    tk.Label(
        pie,
        text="Sistema AL TOQUE  |  Municipalidad de Merlo  |  2025",
        font=("Arial", 11),
        bg="#145a32",
        fg="#a8f0c6"
    ).pack()

    # CUERPO
    cuerpo = tk.Frame(ventana, bg="#1a3a2a")
    cuerpo.pack(expand=True, fill=tk.BOTH)

    tk.Label(
        cuerpo,
        text="IMPUESTOS Y PAGOS",
        font=("Arial", 28, "bold"),
        bg="#1a3a2a",
        fg="#ffffff"
    ).pack(pady=(40, 20))

    opciones = [
        "1  →  Pagar Inmobiliario",
        "2  →  Pagar Patente",
        "3  →  Pagar ABL",
        "4  →  Pagar Domiciliario",
        "5  →  Salir"
    ]

    for opcion in opciones:
        tk.Label(
            cuerpo,
            text=opcion,
            font=("Arial", 20),
            bg="#1a3a2a",
            fg="#a8f0c6",
            anchor="w",
            width=35
        ).pack(pady=8)

    def metodo_pago():
        ventana_metodo = tk.Toplevel()
        ventana_metodo.title("Método de pago")
        ventana.state("zoomed")
        ventana_metodo.configure(bg="#1a3a2a")

        tk.Label(ventana_metodo, text="MÉTODO DE PAGO", font=("Arial", 18, "bold"), bg="#1a3a2a", fg="#ffffff").pack(pady=20)
        tk.Label(ventana_metodo, text="1. Pagar con Tarjeta", font=("Arial", 14), bg="#1a3a2a", fg="#a8f0c6").pack(pady=5)
        tk.Label(ventana_metodo, text="2. Pagar con QR", font=("Arial", 14), bg="#1a3a2a", fg="#a8f0c6").pack(pady=5)
        tk.Label(ventana_metodo, text="3. Cancelar", font=("Arial", 14), bg="#1a3a2a", fg="#ff6b6b").pack(pady=5)

        resultado_metodo = tk.Label(ventana_metodo, text="", font=("Arial", 13), bg="#1a3a2a", fg="#a8f0c6")
        resultado_metodo.pack(pady=10)

        def on_key_Press_metodo(event):
            match event.char:
                case "1":
                    resultado_metodo.config(text="Pago con Tarjeta realizado. Imprimiendo ticket...")
                case "2":
                    resultado_metodo.config(text="Pago con QR realizado. Imprimiendo ticket...")
                case "3":
                    ventana_metodo.destroy()

        ventana_metodo.bind("<KeyPress>", on_key_Press_metodo)
        ventana_metodo.focus_set()

    def abrir_pagos(impuesto, monto):
        ventana_confirmacion = tk.Toplevel()
        ventana_confirmacion.title("Confirmación de pago")
        ventana.state("zoomed")
        ventana_confirmacion.configure(bg="#1a3a2a")

        tk.Label(ventana_confirmacion, text="CONFIRMACIÓN", font=("Arial", 18, "bold"), bg="#1a3a2a", fg="#ffffff").pack(pady=20)
        tk.Label(ventana_confirmacion, text=f"Impuesto: {impuesto}", font=("Arial", 14), bg="#1a3a2a", fg="#a8f0c6").pack(pady=5)
        tk.Label(ventana_confirmacion, text=f"Monto: ${monto}", font=("Arial", 14), bg="#1a3a2a", fg="#a8f0c6").pack(pady=5)
        tk.Label(ventana_confirmacion, text="Presione 1 para pagar  |  2 para cancelar", font=("Arial", 13), bg="#1a3a2a", fg="#6dbf8a").pack(pady=15)

        resultado_confirmacion = tk.Label(ventana_confirmacion, text="", font=("Arial", 13), bg="#1a3a2a", fg="#ff6b6b")
        resultado_confirmacion.pack(pady=10)

        def on_key_Press_confirmacion(event):
            match event.char:
                case "1":                    
                    metodo_pago()
                case "2":
                    ventana_confirmacion.destroy()
                    resultado_confirmacion.config(text="Operación cancelada")

        ventana_confirmacion.bind("<KeyPress>", on_key_Press_confirmacion)
        ventana_confirmacion.focus_set()

    def on_key_Press(event):
        match event.char:
            case "1":
                abrir_pagos("Inmobiliario", ciudadano['imp_inmobiliario'])
            case "2":
                abrir_pagos("Patente", ciudadano['patente'])
            case "3":
                abrir_pagos("ABL", ciudadano['abl'])
            case "4":
                abrir_pagos("Domiciliario", ciudadano['domiciliario'])
            case "5":
                ventana.destroy()

    ventana.bind("<KeyPress>", on_key_Press)
    ventana.focus_set()
