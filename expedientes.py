import tkinter as tk

def VentanaExpedientes(ciudadano):    
    ventana = tk.Toplevel()
    ventana.title("Consulta de Expediente")
    ventana.geometry("450x320")
    ventana.configure(bg="#f8fafc")
    lbl_titulo = tk.Label(ventana, text="Consulta de Expedientes", font=("Arial", 16, "bold"), bg="#f8fafc", fg="#0f172a")
    lbl_titulo.pack(pady=15)
    frame_resultados = tk.Frame(ventana, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
    frame_resultados.pack(fill=tk.X, padx=30, pady=10)
    lbl_numero = tk.label(frame_resultados, text=f"Número de Expediente: {ciudadano['exp_numero']}", font=("Arial", 11), bg="#ffffff", fg="#1e293b")
    lbl_numero.pack(anchor="w")
    lbl_resultado_tramite = tk.Label(frame_resultados, text="Ingrese un número para consultar", font=("Arial", 11, "italic"), bg="#ffffff", fg="#64748b")
    lbl_resultado_tramite.pack(anchor="w")
    lbl_resultado_estado = tk.Label(frame_resultados, text="", font=("Arial", 12, "bold"), bg="#ffffff")
    lbl_resultado_estado.pack(anchor="w", pady=(5, 0))

ventana.focus_set()
