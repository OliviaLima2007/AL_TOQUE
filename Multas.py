import tkinter as tk

def VentanaMultas(ciudadano):
    ventana = tk.Toplevel()
    ventana.title("AL TOQUE - Multas")
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
        text="MULTAS",
        font=("Arial", 28, "bold"),
        bg="#1a3a2a",
        fg="#ffffff"
    ).pack(pady=(40, 20))

    frame_datos = tk.Frame(cuerpo, bg="#145a32", padx=40, pady=30)
    frame_datos.pack(pady=10)

    tk.Label(
        frame_datos,
        text=f"Monto de multas:  {ciudadano['multas']}",
        font=("Arial", 18),
        bg="#145a32",
        fg="#ffffff"
    ).pack(anchor="w", pady=8)

    tk.Label(
        cuerpo,
        text="Presione 1 para consultar  |  Presione 2 para pagar  |  Presione 3 para salir",
        font=("Arial", 16),
        bg="#1a3a2a",
        fg="#6dbf8a"
    ).pack(pady=20)

    resultado = tk.Label(cuerpo, text="", font=("Arial", 14), bg="#1a3a2a", fg="#a8f0c6")
    resultado.pack(pady=10)

    def abrir_consulta():
        resultado.config(text=f"""
        Multas: {ciudadano['multas']}
        Inmobiliario: {ciudadano['imp_inmobiliario']}
        Patente: {ciudadano['patente']}
        ABL: {ciudadano['abl']}
        Domiciliario: {ciudadano['domiciliario']}
        """)

    def metodo_pago():
        ventana_metodo = tk.Toplevel()
        ventana_metodo.state("zoomed")
        ventana_metodo.title("Método de pago")        
        ventana_metodo.configure(bg="#1a3a2a")

        tk.Label(ventana_metodo, text="1. Pagar con Tarjeta", font=("Arial", 14), bg="#1a3a2a", fg="#a8f0c6").pack(pady=10)
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

    def abrir_pago():
        ventana_pago = tk.Toplevel()
        ventana_pago.state("zoomed")
        ancho = 500
        alto = 300
        x = (ventana_pago.winfo_screenwidth()//2) - (ancho//2)
        y = (ventana_pago.winfo_screenheight()//2) - (ancho//2)
        ventana_pago.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana_pago.title("Pago de Multas")        
        ventana_pago.configure(bg="#1a3a2a")

        tk.Label(ventana_pago, text=f"Monto: {ciudadano['multas']}", font=("Arial", 14), bg="#1a3a2a", fg="#ffffff").pack(pady=10)
        tk.Label(ventana_pago, text="Presione 1 para pagar | 2 para cancelar", font=("Arial", 13), bg="#1a3a2a", fg="#6dbf8a").pack(pady=10)

        resultado_pago = tk.Label(ventana_pago, text="", font=("Arial", 13), bg="#1a3a2a", fg="#a8f0c6")
        resultado_pago.pack(pady=10)

        def on_key_Press_pago(event):
            match event.char:
                case "1":
                    metodo_pago()
                case "2":
                    ventana_pago.destroy()

        ventana_pago.bind("<KeyPress>", on_key_Press_pago)
        ventana_pago.focus_set()

    def on_key_Press(event):
        match event.char:
            case "1":
                abrir_consulta()
            case "2":
                abrir_pago()
            case "3":
                ventana.destroy()

    ventana.bind("<KeyPress>", on_key_Press)
    ventana.focus_set()