from tkinter import *
from tkinter import messagebox

# ---------------- FUNCIONES ---------------- #

def abrir_impuestos():

    ventana_impuestos = Toplevel(root)
    ventana_impuestos.title("Impuestos")
    ventana_impuestos.geometry("500x400")
    ventana_impuestos.config(bg="#d9d2ff")

    Label(
        ventana_impuestos,
        text="TABLA DE IMPUESTOS",
        font=("Arial", 18, "bold"),
        bg="#d9d2ff"
    ).pack(pady=15)

    # TABLA INFORMATIVA

    tabla = Frame(ventana_impuestos, bg="black")
    tabla.pack(pady=10)

    datos = [["Impuesto", "Estado", "Monto / Último pago"],
    ["Inmobiliario", "Adeuda", "$25.000"],
    ["Patente", "Pagado","Último pago: $18.000"],
    ["ABL", "Adeuda", "$12.500"],
    ["Multa tránsito", "Pagado",
     "Último pago: $7.500"]]

    for fila in range(len(datos)):
        for columna in range(len(datos[fila])):

            Label(
                tabla,
                text=datos[fila][columna],
                width=18,
                height=2,
                font=("Arial", 11),
                bg="white",
                relief="solid"
            ).grid(row=fila, column=columna)

    Label(
        ventana_impuestos,
        text="Seleccione qué impuesto desea pagar",
        font=("Arial", 12),
        bg="#d9d2ff"
    ).pack(pady=15)

    # SOLO SE PUEDE PAGAR SI ESTÁ ADEUDADO

    Button(
        ventana_impuestos,
        text="Pagar Inmobiliario",
        width=25,
        bg="green",
        fg="white",
        command=lambda: abrir_pagos("Impuesto Inmobiliario", 25000)
    ).pack(pady=5)

    Button(
        ventana_impuestos,
        text="Pagar ABL",
        width=25,
        bg="green",
        fg="white",
        command=lambda: abrir_pagos("ABL", 12500)
    ).pack(pady=5)

    Button(
        ventana_impuestos,
        text="Salir",
        width=25,
        bg="red",
        fg="white",
        command=ventana_impuestos.destroy
    ).pack(pady=15)


def abrir_pagos(impuesto, monto):

    ventana_pagos = Toplevel(root)
    ventana_pagos.title("Pagos")
    ventana_pagos.geometry("400x350")
    ventana_pagos.config(bg="#cfc4ff")

    Label(
        ventana_pagos,
        text="MÓDULO DE PAGOS",
        font=("Arial", 18, "bold"),
        bg="#cfc4ff"
    ).pack(pady=20)

    Label(
        ventana_pagos,
        text=f"Impuesto: {impuesto}",
        font=("Arial", 12),
        bg="#cfc4ff"
    ).pack(pady=5)

    Label(
        ventana_pagos,
        text=f"Monto a pagar: ${monto}",
        font=("Arial", 12),
        bg="#cfc4ff"
    ).pack(pady=5)

    Label(
        ventana_pagos,
        text="Método de pago",
        font=("Arial", 13, "bold"),
        bg="#cfc4ff"
    ).pack(pady=15)

    Button(
        ventana_pagos,
        text="Pagar con tarjeta",
        width=25,
        height=2,
        command=lambda: pagar("Tarjeta")
    ).pack(pady=10)

    Button(
        ventana_pagos,
        text="Pagar con QR",
        width=25,
        height=2,
        command=lambda: pagar("QR")
    ).pack(pady=10)

    Button(
        ventana_pagos,
        text="Cancelar",
        width=25,
        height=2,
        bg="red",
        fg="white",
        command=ventana_pagos.destroy
    ).pack(pady=15)


def pagar(metodo):

    messagebox.showinfo(
        "Pago realizado",
        f"Pago realizado correctamente con {metodo}\n"
        "Imprimiendo ticket..."
    )


# ---------------- VENTANA PRINCIPAL ---------------- #

root = Tk()
root.title("Sistema Municipal")
root.geometry("450x300")
root.config(bg="#cfc4ff")

Label(
    root,
    text="SISTEMA MUNICIPAL",
    font=("Arial", 20, "bold"),
    bg="#cfc4ff"
).pack(pady=30)

Label(
    root,
    text="Seleccione un módulo",
    font=("Arial", 13),
    bg="#cfc4ff"
).pack(pady=10)

# ---------------- BOTONES ---------------- #

Button(
    root,
    text="Impuestos",
    width=30,
    height=3,
    bg="#8e7dff",
    fg="white",
    command=abrir_impuestos
).pack(pady=10)

Button(
    root,
    text="Salir",
    width=30,
    height=3,
    bg="red",
    fg="white",
    command=root.destroy
).pack(pady=10)

# ---------------- EJECUCIÓN ---------------- #

root.mainloop()
