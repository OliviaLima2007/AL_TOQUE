import tkinter as tk
from tkinter import messagebox

# Variable global para controlar en qué paso está el usuario
# Paso 0: Escribiendo el número. Paso 1: Esperando confirmación con '1' o 'Enter'
paso_actual = 0

def procesar_teclado(event):
    global paso_actual
    
    # Obtener el número actual en el cuadro de texto
    numero = entrada_numero.get().strip()

    # --- PASO 1: El usuario está escribiendo y presiona ENTER para fijar el número ---
    if paso_actual == 0 and event.keysym == "Return":
        if not numero:
            messagebox.showwarning("Campo vacío", "Por favor, ingrese un número de expediente.")
            return
        
        # Avanzamos al siguiente paso y cambiamos el mensaje informativo
        paso_actual = 1
        btn_consultar.config(text="¡Número fijado! Presione '1' o 'ENTER' para iniciar la consulta", bg="#ea580c")
        entrada_numero.config(state="disabled") # Bloqueamos la entrada temporalmente para que el '1' no se escriba adentro
        return

    # --- PASO 2: El número ya está fijado, ahora espera que presione '1' o 'Enter' para BUSCAR ---
    if paso_actual == 1:
        if event.char == '1' or event.keysym == "Return":
            consultar_expediente(numero)

def consultar_expediente(numero):
    global paso_actual
    
    # Evaluación dinámica sin base de datos
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
        # Si el número no coincide con ninguno
        lbl_resultado_tramite.config(text="Expediente no encontrado", fg="#dc2626")
        lbl_resultado_estado.config(text="")
        messagebox.showerror("Error", "El número de expediente no existe en el sistema.")
        reiniciar_sistema()
        return

    # Mostrar el resultado en la pantalla de visualización si se encontró
    lbl_resultado_tramite.config(text=f"Trámite: {tramite}", fg="#1e293b")
    lbl_resultado_estado.config(text=f"Estado Actual: {estado}", fg="#2563eb")
    
    # Volver al estado inicial para permitir una nueva consulta
    reiniciar_sistema()

def reiniciar_sistema():
    global paso_actual
    paso_actual = 0
    entrada_numero.config(state="normal")
    entrada_numero.delete(0, tk.END)
    btn_consultar.config(text="Escriba el expediente y presione ENTER", bg="#64748b")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Consulta de Expediente")
ventana.geometry("470(6)x340")
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
entrada_numero.insert(0, "101/2026") # Ejemplo inicial listo para probar
entrada_numero.focus()

# --- CAPTURA DE TECLADO ---
# Ahora una sola función inteligente maneja todo el comportamiento del teclado
ventana.bind("<Key>", procesar_teclado)

# Botón indicador visual que va cambiando de color e instrucciones según el paso
btn_consultar = tk.Button(ventana, text="Escriba el expediente y presione ENTER", font=("Arial", 10, "bold"), bg="#64748b", fg="white", 
                          padx=10, pady=5, state="disabled")
btn_consultar.pack(pady=15)

# --- Pantalla de Visualización de Resultados ---
frame_resultados = tk.Frame(ventana, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
frame_resultados.pack(fill=tk.X, padx=30, pady=10)

lbl_resultado_tramite = tk.Label(frame_resultados, text="Ingrese un número para consultar", font=("Arial", 11, "italic"), bg="#ffffff", fg="#64748b")
lbl_resultado_tramite.pack(anchor="w")

lbl_resultado_estado = tk.Label(frame_resultados, text="", font=("Arial", 12, "bold"), bg="#ffffff")
lbl_resultado_estado.pack(anchor="w", pady=(5, 0))

ventana.mainloop()
