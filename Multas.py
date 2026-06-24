from tkinter import *
from tkinter import messagebox

# ---------------- VENTANA PRINCIPAL ---------------- #

root = Tk()
root.title("Sistema Municipal")
root.geometry("600x400")

# ---------------- FUNCIONES ---------------- #

def turnos_tramites():
    ventana = Toplevel(root)
    ventana.title("Turnos y Estado de Trámite")
    ventana.geometry("400x300")

    Label(ventana, text="Turnos y Estado de Trámite",
          font=("Arial", 14, "bold")).pack(pady=10)

    Button(
        ventana,
        text="Sacar turno para trámites presenciales",
        command=lambda: messagebox.showinfo(
            "Turno", "Turno generado correctamente")
    ).pack(pady=10)

    Button(
        ventana,
        text="Consultar estado de trámite",
        command=consultar_tramite
    ).pack(pady=10)


def consultar_tramite():
    ventana = Toplevel(root)
    ventana.title("Consultar Trámite")

    Label(ventana, text="Ingrese número de expediente").pack(pady=10)

    expediente = Entry(ventana)
    expediente.pack()

    Button(
        ventana,
        text="Consultar",
        command=lambda: messagebox.showinfo(
            "Resultado",
            f"Estado del expediente {expediente.get()}: En revisión"
        )
    ).pack(pady=10)


# ---------------- IMPUESTOS ---------------- #

def impuestos():
    ventana = Toplevel(root)
    ventana.title("Impuestos y Pagos")
    ventana.geometry("400x300")

    Label(
        ventana,
        text="Seleccione una opción",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    Button(
        ventana,
        text="Pagar impuesto inmobiliario",
        command=lambda: pago("Impuesto inmobiliario")
    ).pack(pady=5)

    Button(
        ventana,
        text="Pagar patente auto/moto",
        command=lambda: pago("Patente")
    ).pack(pady=5)

    Button(
        ventana,
        text="Pagar ABL",
        command=lambda: pago("ABL")
    ).pack(pady=5)

    Button(
        ventana,
        text="Consultar deuda total",
        command=lambda: messagebox.showinfo(
            "Deuda", "Deuda total: $25.000")
    ).pack(pady=5)


def pago(concepto):
    respuesta = messagebox.askyesno(
        "Pago",
        f"Debe dinero por {concepto}\n¿Desea pagar?"
    )

    if respuesta:
        metodo_pago()
    else:
        messagebox.showinfo(
            "Cancelar",
            "Volviendo al menú de Impuestos"
        )


# ---------------- MULTAS ---------------- #

def multas():
    ventana = Toplevel(root)
    ventana.title("Multas")
    ventana.geometry("400x300")

    Label(
        ventana,
        text="Multas",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    Button(
        ventana,
        text="Consultar multas de tránsito",
        command=consultar_multas
    ).pack(pady=10)

    Button(
        ventana,
        text="Pagar multas de tránsito",
        command=pagar_multa
    ).pack(pady=10)


def consultar_multas():
    messagebox.showinfo(
        "Multas",
        "Multa 1: $15.000\nMulta 2: $8.000"
    )


def pagar_multa():
    respuesta = messagebox.askyesno(
        "Pago de Multas",
        "Debe dinero. ¿Desea pagar?"
    )

    if respuesta:
        metodo_pago()
    else:
        messagebox.showinfo(
            "Salir",
            "Volviendo al menú de multas"
        )


# ---------------- MÉTODO DE PAGO ---------------- #

def metodo_pago():
    ventana = Toplevel(root)
    ventana.title("Método de Pago")
    ventana.geometry("300x200")

    Label(
        ventana,
        text="Seleccione método de pago"
    ).pack(pady=15)

    Button(
        ventana,
        text="Pagar con QR",
        command=pago_qr
    ).pack(pady=10)

    Button(
        ventana,
        text="Pagar con Tarjeta",
        command=pago_tarjeta
    ).pack(pady=10)


def pago_qr():
    messagebox.showinfo(
        "QR",
        "Se habilita código QR"
    )

    messagebox.showinfo(
        "Ticket",
        "Imprimiendo ticket..."
    )


def pago_tarjeta():
    aceptar = messagebox.askyesno(
        "Tarjeta",
        "¿Confirmar pago con tarjeta?"
    )

    if aceptar:
        messagebox.showinfo(
            "POSNET",
            "Se habilita el POSNET"
        )

        messagebox.showinfo(
            "Ticket",
            "Imprimiendo ticket..."
        )
    else:
        messagebox.showinfo(
            "Cancelar",
            "Operación cancelada"
        )


# ---------------- BIENVENIDA ---------------- #

Label(
    root,
    text="¡Bienvenido! Ingrese su DNI",
    font=("Arial", 16, "bold")
).pack(pady=20)

dni = Entry(root, width=30)
dni.pack()

Button(
    root,
    text="Turnos y Estado de Trámite",
    width=30,
    command=turnos_tramites
).pack(pady=10)

Button(
    root,
    text="Impuestos y Pagos",
    width=30,
    command=impuestos
).pack(pady=10)

Button(
    root,
    text="Multas",
    width=30,
    command=multas
).pack(pady=10)

root.mainloop()