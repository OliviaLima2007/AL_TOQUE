import tkinter as tk
from tkinter import messagebox

# "Base de datos" simulada con algunos expedientes de prueba
# Estructura: 'Numero_Expediente': ('Tipo de Trámite', 'Estado Actual')
base_datos_expedientes = {
    "101/2026": ("Divorcio de mutuo acuerdo", "En calificación judicial"),
    "202/2026": ("Habilitación de comercio", "Aprobado - Listo para retirar"),
    "303/2026": ("Demanda laboral", "En etapa de mediación"),
    "404/2026": ("Inscripción de propiedad", "Rechazado por falta de documentación"),
}

def consultar_expediente():
    # Obtener el número ingresado por el usuario
    numero = entrada_numero.get().strip()
    
    if not numero:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese un número de expediente.")
        return
    
    # Buscar en la "base de datos"
    if numero in base_datos_expedientes:
        tramite, estado = base_datos_expedientes[numero]
        # Actualizar las etiquetas con el resultado
        lbl_resultado_tramite.config(text=f"Trámite: {tramite}", fg="#1e293b")
        lbl_resultado_estado.config(text=f"Estado Actual: {estado}", fg="#2563eb") # Azul para resaltar
    else:
        # Si no lo encuentra, limpia el resultado y avisa
        lbl_resultado_tramite.config(text="Expediente no encontrado", fg="#dc2626") # Rojo
        lbl_resultado_estado.config(text="")
        messagebox.onerror("Error", "El número de expediente no existe en el sistema.")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Sistema de Consulta de Expedientes")
ventana.geometry("450x320")
ventana.configure(bg="#f8fafc") # Fondo gris claro moderno

# --- Componentes de la Interfaz (Widgets) ---

# Título principal
lbl_titulo = tk.Label(ventana, text="Consulta de Expedientes", font=("Arial", 16, "bold"), bg="#f8fafc", fg="#0f172a")
lbl_titulo.pack(pady=15)

# Contenedor para la entrada
frame_entrada = tk.Frame(ventana, bg="#f8fafc")
frame_entrada.pack(pady=10)

lbl_instruccion = tk.Label(frame_entrada, text="Número de Expediente:", font=("Arial", 11), bg="#f8fafc", fg="#475569")
lbl_instruccion.pack(side=tk.LEFT, padx=5)

entrada_numero = tk.Entry(frame_entrada, font=("Arial", 11), width=15, bd=2, relief="groove")
entrada_numero.pack(side=tk.LEFT, padx=5)
entrada_numero.insert(0, "101/2026") # Texto de ejemplo inicial

# Botón de consulta
btn_consultar = tk.Button(ventana, text="Buscar Estado", font=("Arial", 11, "bold"), bg="#2563eb", fg="white", 
                          padx=10, pady=5, activebackground="#1d4ed8", activeforeground="white", cursor="hand2", command=consultar_expediente)
btn_consultar.pack(pady=15)

# --- Zona de Visualización de Resultados ---
frame_resultados = tk.Frame(ventana, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
frame_resultados.pack(fill=tk.X, padx=30, pady=10)

lbl_resultado_tramite = tk.Label(frame_resultados, text="Ingrese un número para consultar", font=("Arial", 11, "italic"), bg="#ffffff", fg="#64748b")
lbl_resultado_tramite.pack(anchor="w")

lbl_resultado_estado = tk.Label(frame_resultados, text="", font=("Arial", 12, "bold"), bg="#ffffff")
lbl_resultado_estado.pack(anchor="w", pady=(5, 0))

# Iniciar el bucle de la aplicación
ventana.mainloop()
