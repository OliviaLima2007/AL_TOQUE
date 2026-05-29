import tkinter as tk
from tkinter import messagebox

def consultar_expediente(event=None):
    # Obtener el número ingresado por el usuario y quitar espacios
    numero = entrada_numero.get().strip()
    
    # Si el usuario escribió un '1' al final o solo un '1', lo limpiamos para evaluar el expediente real
    # o activamos la búsqueda directamente.
    if numero.endswith('1'):
        # Si termina en 1 (por ejemplo "101/20261" o solo "1"), le quitamos ese 1 para buscar el expediente real
        if len(numero) > 1:
            numero = numero[:-1].strip()
        else:
            messagebox.showwarning("Campo vacío", "Por favor, ingrese un número de expediente válido antes del 1.")
            return

    # Validación: Verificar si el campo está vacío
    if not numero:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese un número de expediente.")
        return
    
    # Evaluación dinámica sin base de datos (Estructura de control directa)
    if numero == "101/2026":
        tramite = "Multa"
        estado = "En proceso"
    elif numero == "202/2026":
        tramite = "Pago de patentes"
        estado = "En revision"
    elif numero == "303/2026":
        tramite = "pago de impuestas inmoviliarios"
        estado = "No iniciado"
    else:
        # Si el número no coincide con ninguno de los anteriores
        lbl_resultado_tramite.config(text="Expediente no encontrado", fg="#dc2626")
        lbl_resultado_estado.config(text="")
        messagebox.showerror("Error", "El número de expediente no existe en el sistema.")
        return

    # Mostrar el resultado en la pantalla de visualización si se encontró
    lbl_resultado_tramite.config(text=f"Trámite: {tramite}", fg="#1e293b")
    lbl_resultado_estado.config(text=f"Estado Actual: {estado}", fg="#2563eb")

def evaluar_tecla(event):
    # Esta función revisa en tiempo real qué escribe el usuario
    # Si presiona la tecla '1', ejecuta la búsqueda automáticamente
    if event.char == '1':
        consultar_expediente()

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

# --- CAPTURA DE TECLADO (REEMPLAZA AL BOTÓN CLICK) ---
# 1. Si el usuario escribe el número "1", se dispara la búsqueda
entrada_numero.bind("<Key>", evaluar_tecla)
# 2. Por comodidad, si presiona la tecla "Enter" (Return) también busca
entrada_numero.bind("<Return>", consultar_expediente)

# Modificamos el texto del botón para avisar que ahora es con teclado (y quitamos el comando de click directo)
btn_consultar = tk.Button(ventana, text="Presione ENTER o '1' para buscar", font=("Arial", 11, "bold"), bg="#64748b", fg="white", 
                          padx=10, pady=5, state="disabled") # Queda como indicador visual informativo
btn_consultar.pack(pady=15)

# --- Pantalla de Visualización de Resultados ---
frame_resultados = tk.Frame(ventana, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
frame_resultados.pack(fill=tk.X, padx=30, pady=10)

lbl_resultado_tramite = tk.Label(frame_resultados, text="Ingrese un número para consultar", font=("Arial", 11, "italic"), bg="#ffffff", fg="#64748b")
lbl_resultado_tramite.pack(anchor="w")

lbl_resultado_estado = tk.Label(frame_resultados, text="", font=("Arial", 12, "bold"), bg="#ffffff")
lbl_resultado_estado.pack(anchor="w", pady=(5, 0))

ventana.mainloop()
