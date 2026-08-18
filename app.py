import tkinter as tk
from tkinter import messagebox


# ==========================================
# FUNCIÓN DEL BOTÓN ACEPTAR
# ==========================================

def aceptar():

    # Obtener las respuestas
    primera = respuesta1.get()
    segunda = respuesta2.get()

    # Verificar que ambas preguntas hayan sido respondidas
    if primera == "" or segunda == "":
        messagebox.showwarning(
            "Faltan respuestas",
            "Por favor responda las dos preguntas."
        )
        return

    # Crear el mensaje final
    mensaje = (
        f"Su primera respuesta fue {primera} "
        f"y su segunda respuesta fue {segunda}."
    )

    # Mostrar el resultado
    messagebox.showinfo(
        "Resultado",
        mensaje
    )


# ==========================================
# CREAR LA VENTANA PRINCIPAL
# ==========================================

ventana = tk.Tk()

ventana.title("Formulario de preguntas")

# Tamaño de la ventana
ventana.geometry("500x400")

# Evitar que el usuario cambie el tamaño
ventana.resizable(False, False)


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="Formulario de preguntas",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=20)


# ==========================================
# PREGUNTA 1
# ==========================================

pregunta1_label = tk.Label(
    ventana,
    text="¿Tiene experiencia en Python?",
    font=("Arial", 12)
)

pregunta1_label.pack(pady=10)


# Variable donde se guardará la respuesta
respuesta1 = tk.StringVar(value="")


# Opción Sí
radio_si_1 = tk.Radiobutton(
    ventana,
    text="Sí",
    variable=respuesta1,
    value="Sí",
    font=("Arial", 11)
)

radio_si_1.pack()


# Opción No
radio_no_1 = tk.Radiobutton(
    ventana,
    text="No",
    variable=respuesta1,
    value="No",
    font=("Arial", 11)
)

radio_no_1.pack()


# ==========================================
# PREGUNTA 2
# ==========================================

pregunta2_label = tk.Label(
    ventana,
    text="¿Tiene experiencia en SQL?",
    font=("Arial", 12)
)

pregunta2_label.pack(pady=10)


# Variable donde se guardará la respuesta
respuesta2 = tk.StringVar(value="")


# Opción Sí
radio_si_2 = tk.Radiobutton(
    ventana,
    text="Sí",
    variable=respuesta2,
    value="Sí",
    font=("Arial", 11)
)

radio_si_2.pack()


# Opción No
radio_no_2 = tk.Radiobutton(
    ventana,
    text="No",
    variable=respuesta2,
    value="No",
    font=("Arial", 11)
)

radio_no_2.pack()


# ==========================================
# BOTÓN ACEPTAR
# ==========================================

boton_aceptar = tk.Button(
    ventana,
    text="Aceptar",
    command=aceptar,
    font=("Arial", 11, "bold"),
    width=15,
    height=1
)

boton_aceptar.pack(pady=25)


# ==========================================
# INICIAR LA APLICACIÓN
# ==========================================

ventana.mainloop()