def agregar_numero(numero):
    entrada.insert(END, numero)


def borrar():
    entrada.delete(0, END)


def aceptar():
    opcion = entrada.get()

    if opcion == "1":
        mostrar_pago("Impuesto inmobiliario")

    elif opcion == "2":
        mostrar_pago("Patente auto o moto")

    elif opcion == "3":
        mostrar_pago("ABL")

    elif opcion == "4":
        consultar_deuda()

    else:
        messagebox.showerror("Error", "Opción inválida")

    entrada.delete(0, END)


def mostrar_pago(tipo):
    ventana = Toplevel(root)
    ventana.title("Pago")
    ventana.geometry("400x300")
    ventana.config(bg="#d9d2ff")

    Label(
        ventana,
        text=f"{tipo}",
        font=("Arial", 14, "bold"),
        bg="#d9d2ff"
    ).pack(pady=20)

    Label(
        ventana,
        text="Ingrese método de pago:\n1 = Tarjeta\n2 = QR",
        font=("Arial", 12),
        bg="#d9d2ff"
    ).pack(pady=10)

    entrada_pago = Entry(ventana, font=("Arial", 16), justify="center")
    entrada_pago.pack(pady=10)

    def procesar_pago():
        metodo = entrada_pago.get()

        if metodo == "1":
            messagebox.showinfo(
                "Pago",
                "Pago con tarjeta aprobado\nImprimiendo ticket..."
            )

        elif metodo == "2":
            messagebox.showinfo(
                "QR",
                "QR habilitado para pagar"
            )

        else:
            messagebox.showerror("Error", "Método inválido")

    Button(
        ventana,
        text="Aceptar",
        width=15,
        command=procesar_pago
    ).pack(pady=10)


def consultar_deuda():
    messagebox.showinfo(
        "Deuda total",
        "Impuesto inmobiliario: $25.000\n"
        "Patente: $18.000\n"
        "ABL: $12.500"
    )

root = Tk()
root.title("Sistema de Impuestos y Pagos")
root.geometry("400x550")
root.config(bg="#cfc4ff")

Label(
    root,
    text="IMPUESTOS Y PAGOS",
    font=("Arial", 18, "bold"),
    bg="#cfc4ff"
).pack(pady=20)

Label(
    root,
    text=(
        "1 - Impuesto inmobiliario\n"
        "2 - Patente auto o moto\n"
        "3 - ABL\n"
        "4 - Consultar deuda"
    ),
    font=("Arial", 12),
    bg="#cfc4ff",
    justify=LEFT
).pack(pady=10)

entrada = Entry(root, font=("Arial", 20), justify="center")
entrada.pack(pady=20)
