import tkinter as tk

def VentanaExpedientes(ciudadano):
    ventana = tk.Toplevel()
    ventana.title("AL TOQUE - Expedientes")
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
        text="CONSULTA DE EXPEDIENTES",
        font=("Arial", 28, "bold"),
        bg="#1a3a2a",
        fg="#ffffff"
    ).pack(pady=(40, 30))

    frame_datos = tk.Frame(cuerpo, bg="#145a32", padx=40, pady=30)
    frame_datos.pack(pady=10)

    tk.Label(
        frame_datos,
        text=f"Número de Expediente:  {ciudadano['exp_numero']}",
        font=("Arial", 18),
        bg="#145a32",
        fg="#ffffff"
    ).pack(anchor="w", pady=8)

    tk.Label(
        frame_datos,
        text=f"Trámite:  {ciudadano['exp_tramite']}",
        font=("Arial", 18),
        bg="#145a32",
        fg="#a8f0c6"
    ).pack(anchor="w", pady=8)

    tk.Label(
        frame_datos,
        text=f"Estado Actual:  {ciudadano['exp_estado']}",
        font=("Arial", 18, "bold"),
        bg="#145a32",
        fg="#d4f5e2"
    ).pack(anchor="w", pady=8)

    ventana.focus_set()