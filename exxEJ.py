import tkinter as tk
from tkinter import messagebox

def consultar_expediente():
    # Obtener el número ingresado por el usuario y quitar espacios
    numero = entrada_numero.get().strip()
    
    # Validación: Verificar si el campo está vacío
    if not numero:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese un número de expediente.")
        return
    
    # Evaluación dinámica sin base de datos (Estructura de control directa)
    if numero == "101/2026":
        tramite = "Divorcio de mutuo acuerdo"
        estado = "En calificación judicial"
    elif numero == "202/2026":
        tramite = "Habilitación de comercio"
        estado = "Aprobado - Listo para retirar"
    elif numero == "303/2026":
        tramite = "Demanda laboral"
        estado = "En etapa de mediación"
    else:
        # Si el número no coincide con ninguno de los anteriores
        lbl_resultado_tramite.config(text="Expediente no encontrado", fg="#dc2626")
        lbl_resultado_estado.config(text="")
        messagebox.showerror("Error", "El número de expediente no existe en el sistema.")
        return

    # Mostrar el resultado en la pantalla de visualización si se encontró
    lbl_resultado_tramite.config(text=f"Trámite: {tramite}", fg="#1e293b")
    lbl_resultado_estado.config(text=f"Estado Actual: {estado}", fg="#2563eb")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Consulta de Expediente")
ventana.geometry("450x320")
ventana.configure(bg="#f8fafc")

# --- Componentes de la Interfaz ---
lbl_titulo = tk.Label(ventana, text="Consulta de Expedientes", font=("Arial", 16, "bold"), bg="#f8fafc", fg="#0f172a")
lbl_titulo.pack(pady=15)

frame_entrada = tk.Frame(ventana, bg="#f8fafc")
frame_entrada.pack(pady=10)

lbl_instruccion = tk.Label(frame_entrada, text="Número de Expediente:", font=("Arial", 11), bg="#f8fafc", fg="#475569")
lbl_instruccion.pack(side=tk.LEFT, padx=5)

entrada_numero = tk.Entry(frame_entrada, font=("Arial", 11), width=15, bd=2, relief="groove")
entrada_numero.pack(side=tk.LEFT, padx=5)
entrada_numero.insert(0, "101/2026") # Ejemplo por defecto para probar rápido

btn_consultar = tk.Button(ventana, text="Buscar Estado", font=("Arial", 11, "bold"), bg="#2563eb", fg="white", 
                          padx=10, pady=5, activebackground="#1d4ed8", activeforeground="white", cursor="hand2", command=consultar_expediente)
btn_consultar.pack(pady=15)

# --- Pantalla de Visualización de Resultados ---
frame_resultados = tk.Frame(ventana, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
frame_resultados.pack(fill=tk.X, padx=30, pady=10)

lbl_resultado_tramite = tk.Label(frame_resultados, text="Ingrese un número para consultar", font=("Arial", 11, "italic"), bg="#ffffff", fg="#64748b")
lbl_resultado_tramite.pack(anchor="w")

lbl_resultado_estado = tk.Label(frame_resultados, text="", font=("Arial", 12, "bold"), bg="#ffffff")
lbl_resultado_estado.pack(anchor="w", pady=(5, 0))

ventana.mainloop()
