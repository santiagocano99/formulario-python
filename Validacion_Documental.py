import tkinter as tk
from tkinter import messagebox


# ============================================================
# CONFIGURACIÓN VISUAL
# ============================================================

COLOR_FONDO = "#F4F7FB"
COLOR_TARJETA = "#FFFFFF"
COLOR_AZUL_OSCURO = "#123B6D"
COLOR_AZUL = "#1976D2"
COLOR_AZUL_CLARO = "#EAF3FF"
COLOR_TEXTO = "#172B4D"
COLOR_TEXTO_SECUNDARIO = "#64748B"
COLOR_BORDE = "#D9E2EC"
COLOR_BLANCO = "#FFFFFF"

# Colores para resaltar el resultado
COLOR_RESALTADO_AMARILLO = "#FFF59D"
COLOR_RESALTADO_VERDE = "#C8E6C9"


# ============================================================
# PREGUNTAS Y DOCUMENTOS
# ============================================================

preguntas_documentos = [
    {
        "pregunta": (
            "¿La iniciativa contempla el lanzamiento o modificación de un "
            "producto o servicio cuyos clientes o usuarios deban aceptar "
            "condiciones de uso, derechos, obligaciones o restricciones?"
        ),
        "documento": "Reglamento / Términos y Condiciones (T&C) de Producto"
    },
    {
        "pregunta": (
            "¿La iniciativa requiere una guía formal que describa las "
            "actividades, responsables y pasos necesarios para implementar "
            "la solución?"
        ),
        "documento": "Procedimiento de Implementación"
    },
    {
        "pregunta": (
            "¿La iniciativa requiere socializar o promocionar comercialmente "
            "el producto o servicio ante clientes potenciales o áreas de negocio?"
        ),
        "documento": "Presentación Comercial"
    },
    {
        "pregunta": (
            "¿La iniciativa requiere presentar una propuesta formal con "
            "alcance, condiciones y/o precios para uno o más clientes?"
        ),
        "documento": "Oferta Comercial"
    },
    {
        "pregunta": (
            "¿La iniciativa genera cobros a clientes o modifica la forma "
            "en que se realizará la facturación de un producto o servicio?"
        ),
        "documento": "Procedimiento de Facturación"
    },
    {
        "pregunta": (
            "¿La iniciativa introduce un nuevo producto, servicio o cambio "
            "significativo que pueda generar riesgos operativos, tecnológicos, "
            "financieros, legales o reputacionales?"
        ),
        "documento": "Matriz de Riesgos del Producto"
    },
    {
        "pregunta": (
            "¿La iniciativa requiere definir cómo serán gestionados, "
            "clasificados y atendidos los incidentes asociados al producto "
            "o servicio?"
        ),
        "documento": "Matriz de Atención de Incidentes"
    },
    {
        "pregunta": (
            "¿La iniciativa requiere integraciones con sistemas internos, "
            "externos, APIs, plataformas o componentes tecnológicos que "
            "deban documentarse técnicamente?"
        ),
        "documento": "Especificaciones Técnicas o Manual de Integración"
    },
    {
        "pregunta": (
            "¿La iniciativa requiere definir niveles de soporte, responsables "
            "y tiempos de atención para solicitudes o requerimientos de "
            "usuarios o clientes?"
        ),
        "documento": "Matriz de Escalamiento o Atención de Solicitudes"
    },
    {
        "pregunta": (
            "¿La iniciativa crea, captura, almacena, transforma, comparte "
            "o elimina datos personales, confidenciales o de negocio durante "
            "su operación?"
        ),
        "documento": "Formulario Ciclo de Vida del Dato"
    }
]


# ============================================================
# VARIABLES
# ============================================================

respuestas_si_no = []


# ============================================================
# FUNCIÓN PARA COPIAR TEXTO
# ============================================================

def copiar_texto(texto, ventana_resultado):

    ventana_resultado.clipboard_clear()
    ventana_resultado.clipboard_append(texto)
    ventana_resultado.update()

    messagebox.showinfo(
        "Copiado",
        "El resultado fue copiado al portapapeles.",
        parent=ventana_resultado
    )


# ============================================================
# MOSTRAR RESULTADO
# ============================================================

def mostrar_resultado(
    mensaje,
    nombre_iniciativa,
    categorias_requeridas
):

    ventana_resultado = tk.Toplevel(ventana)

    ventana_resultado.title("Resultado")
    ventana_resultado.geometry("850x650")

    ventana_resultado.configure(
        bg=COLOR_FONDO
    )

    ventana_resultado.resizable(
        True,
        True
    )

    ventana_resultado.transient(
        ventana
    )

    # --------------------------------------------------------
    # ENCABEZADO
    # --------------------------------------------------------

    encabezado = tk.Frame(
        ventana_resultado,
        bg=COLOR_AZUL_OSCURO,
        height=90
    )

    encabezado.pack(
        fill="x"
    )

    encabezado.pack_propagate(
        False
    )

    titulo = tk.Label(
        encabezado,
        text="Resultado de la evaluación",
        font=("Arial", 18, "bold"),
        bg=COLOR_AZUL_OSCURO,
        fg=COLOR_BLANCO
    )

    titulo.pack(
        pady=(18, 2)
    )

    subtitulo = tk.Label(
        encabezado,
        text="Prompt generado para búsqueda en DocManagement",
        font=("Arial", 10),
        bg=COLOR_AZUL_OSCURO,
        fg="#D9E8F8"
    )

    subtitulo.pack()

    # --------------------------------------------------------
    # CONTENEDOR
    # --------------------------------------------------------

    contenedor = tk.Frame(
        ventana_resultado,
        bg=COLOR_FONDO
    )

    contenedor.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=20
    )

    # --------------------------------------------------------
    # TEXTO
    # --------------------------------------------------------

    texto_resultado = tk.Text(
        contenedor,
        font=("Arial", 10),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO,
        relief="flat",
        bd=0,
        wrap="word",
        padx=15,
        pady=15,
        highlightthickness=1,
        highlightbackground=COLOR_BORDE
    )

    texto_resultado.pack(
        side="left",
        fill="both",
        expand=True
    )

    # --------------------------------------------------------
    # SCROLLBAR
    # --------------------------------------------------------

    scrollbar_resultado = tk.Scrollbar(
        contenedor,
        orient="vertical",
        command=texto_resultado.yview
    )

    scrollbar_resultado.pack(
        side="right",
        fill="y"
    )

    texto_resultado.configure(
        yscrollcommand=scrollbar_resultado.set
    )

    # --------------------------------------------------------
    # INSERTAR TEXTO
    # --------------------------------------------------------

    texto_resultado.insert(
        "1.0",
        mensaje
    )

    # ========================================================
    # RESALTAR RESPUESTA 1 EN AMARILLO
    # ========================================================

    if nombre_iniciativa:

        inicio_busqueda = "1.0"

        while True:

            posicion = texto_resultado.search(
                nombre_iniciativa,
                inicio_busqueda,
                stopindex=tk.END,
                nocase=False
            )

            if not posicion:
                break

            final = f"{posicion}+{len(nombre_iniciativa)}c"

            texto_resultado.tag_add(
                "resaltado_amarillo",
                posicion,
                final
            )

            inicio_busqueda = final

    texto_resultado.tag_configure(
        "resaltado_amarillo",
        background=COLOR_RESALTADO_AMARILLO
    )

    # ========================================================
    # RESALTAR TODAS LAS CATEGORÍAS SELECCIONADAS EN VERDE
    # ========================================================

    for documento in categorias_requeridas:

        inicio_busqueda = "1.0"

        while True:

            posicion = texto_resultado.search(
                documento,
                inicio_busqueda,
                stopindex=tk.END,
                nocase=False
            )

            if not posicion:
                break

            final = f"{posicion}+{len(documento)}c"

            texto_resultado.tag_add(
                "resaltado_verde",
                posicion,
                final
            )

            inicio_busqueda = final

    texto_resultado.tag_configure(
        "resaltado_verde",
        background=COLOR_RESALTADO_VERDE
    )

    # --------------------------------------------------------
    # PERMITIR SELECCIONAR Y COPIAR
    # --------------------------------------------------------

    texto_resultado.config(
        state="normal"
    )

    texto_resultado.focus_set()

    # ========================================================
    # BOTONES
    # ========================================================

    botones = tk.Frame(
        ventana_resultado,
        bg=COLOR_FONDO
    )

    botones.pack(
        pady=(0, 20)
    )

    boton_copiar = tk.Button(
        botones,
        text="  Copiar resultado  ",
        command=lambda: copiar_texto(
            mensaje,
            ventana_resultado
        ),
        font=("Arial", 11, "bold"),
        bg=COLOR_AZUL,
        fg=COLOR_BLANCO,
        activebackground=COLOR_AZUL_OSCURO,
        activeforeground=COLOR_BLANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=15,
        pady=8
    )

    boton_copiar.pack(
        side="left",
        padx=8
    )

    boton_cerrar = tk.Button(
        botones,
        text="  Cerrar  ",
        command=ventana_resultado.destroy,
        font=("Arial", 11),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO,
        activebackground="#E8EEF5",
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=20,
        pady=8,
        highlightthickness=1,
        highlightbackground=COLOR_BORDE
    )

    boton_cerrar.pack(
        side="left",
        padx=8
    )


# ============================================================
# FUNCIÓN ACEPTAR
# ============================================================

def aceptar():

    # --------------------------------------------------------
    # OBTENER INFORMACIÓN
    # --------------------------------------------------------

    nombre_iniciativa = entrada_nombre.get().strip()
    subproceso = entrada_subproceso.get().strip()

    # --------------------------------------------------------
    # VALIDAR NOMBRE DE INICIATIVA
    # --------------------------------------------------------

    if not nombre_iniciativa:

        messagebox.showwarning(
            "Información pendiente",
            "Por favor ingresa el nombre de la iniciativa, producto, servicio, proceso o tema.",
            parent=ventana
        )

        entrada_nombre.focus_set()

        return

    # --------------------------------------------------------
    # VALIDAR SUBPROCESO
    # --------------------------------------------------------

    if not subproceso:

        messagebox.showwarning(
            "Información pendiente",
            "Por favor ingresa el Subproceso objetivo.",
            parent=ventana
        )

        entrada_subproceso.focus_set()

        return

    # --------------------------------------------------------
    # VALIDAR LAS 10 PREGUNTAS
    # --------------------------------------------------------

    respuestas = []

    for i, variable in enumerate(respuestas_si_no):

        respuesta = variable.get()

        if respuesta == "":

            messagebox.showwarning(
                "Respuesta pendiente",
                f"Por favor responde la pregunta {i + 3}.",
                parent=ventana
            )

            return

        respuestas.append(
            respuesta
        )

    # --------------------------------------------------------
    # OBTENER CATEGORÍAS MARCADAS COMO "SÍ"
    # --------------------------------------------------------

    categorias_requeridas = []

    for i, respuesta in enumerate(respuestas):

        if respuesta == "Sí":

            categorias_requeridas.append(
                preguntas_documentos[i]["documento"]
            )

    # --------------------------------------------------------
    # TEXTO DE CATEGORÍAS
    # --------------------------------------------------------

    if categorias_requeridas:

        categorias_texto = "\n".join(
            f"• {categoria}"
            for categoria in categorias_requeridas
        )

        categorias_parentesis = ", ".join(
            categorias_requeridas
        )

    else:

        categorias_texto = (
            "No se marcó ninguna categoría como requerida."
        )

        categorias_parentesis = (
            "ninguna categoría fue marcada como Sí"
        )

    # ========================================================
    # CONSTRUIR PROMPT
    # ========================================================

    mensaje = f"""Realiza una búsqueda exhaustiva en DocManagement sobre:

TEMA: {nombre_iniciativa}
SUBPROCESO OBJETIVO: {subproceso}

Busca coincidencias en nombre, código, contenido, metadatos, anexos, referencias, títulos, tablas, OCR, documentos relacionados, procesos y subprocesos.


FASE 1: IDENTIFICACIÓN

Identifica todos los documentos relacionados con {nombre_iniciativa} sin excluir ninguno por estado, vigencia, clasificación, confidencialidad, borrador o formalidad.

La relación puede establecerse mediante coincidencia exacta, sinónimos, acrónimos, abreviaturas, nombres comerciales, nombres técnicos y referencias asociadas.

Para cada documento incluido muestra:

- Nombre del documento.
- Subproceso.
- Evidencia encontrada.
- Fragmento textual relevante.


FASE 2: CLASIFICACIÓN

Clasifica los documentos según la categoría que mejor corresponda.

{categorias_texto}


RESULTADO

Debes generar obligatoriamente DOS SECCIONES INDEPENDIENTES:


SECCIÓN 1: DOCUMENTOS DONDE COINCIDEN TEMA Y SUBPROCESO OBJETIVO

Incluir únicamente documentos relacionados con {nombre_iniciativa} y cuyo subproceso sea {subproceso}.

Agrupar utilizando las siguientes categorías:

{categorias_texto}

Para cada categoría mostrar:

- Documentos encontrados.
- Subproceso.
- Evidencia.
- Fragmento textual.
- Motivo de clasificación.

Si no existen documentos indicar:

No se encontraron documentos para esta categoría.


SECCIÓN 2: DOCUMENTOS RELACIONADOS CON EL TEMA (SIN FILTRO DE SUBPROCESO)

Incluir todos los documentos relacionados con {nombre_iniciativa}, independientemente del subproceso.

Agrupar utilizando las siguientes categorías:

{categorias_texto}

Para cada categoría mostrar:

- Documentos encontrados.
- Subproceso.
- Evidencia.
- Fragmento textual.
- Motivo de clasificación.

Si no existen documentos indicar:

No se encontraron documentos para esta categoría.


DOCUMENTOS RELACIONADOS NO CLASIFICADOS

Incluir todos los documentos relacionados con {nombre_iniciativa} que no puedan asociarse a ninguna categoría.


VALIDACIONES OBLIGATORIAS

- Todos los documentos encontrados fueron evaluados.
- La Sección 1 contiene únicamente documentos donde coinciden tema y subproceso objetivo.
- La Sección 2 contiene todos los documentos relacionados con el tema independientemente del subproceso.
- Todas las categorías seleccionadas aparecen en ambas secciones.
- Ninguna categoría fue omitida.
- Ningún documento relevante quedó por fuera.
- Todos los documentos incluidos contienen evidencia verificable de relación con el tema buscado.
"""

    # --------------------------------------------------------
    # MOSTRAR RESULTADO
    # --------------------------------------------------------

    mostrar_resultado(
        mensaje,
        nombre_iniciativa,
        categorias_requeridas
    )


# ============================================================
# CREAR VENTANA PRINCIPAL
# ============================================================

ventana = tk.Tk()

ventana.title(
    "Evaluación de Iniciativas"
)

ventana.geometry(
    "950x820"
)

ventana.minsize(
    750,
    650
)

ventana.configure(
    bg=COLOR_FONDO
)


# ============================================================
# ENCABEZADO
# ============================================================

header = tk.Frame(
    ventana,
    bg=COLOR_AZUL_OSCURO,
    height=110
)

header.pack(
    fill="x"
)

header.pack_propagate(
    False
)


titulo_principal = tk.Label(
    header,
    text="Evaluación de Iniciativas",
    font=("Arial", 22, "bold"),
    bg=COLOR_AZUL_OSCURO,
    fg=COLOR_BLANCO
)

titulo_principal.pack(
    pady=(22, 2)
)


subtitulo_principal = tk.Label(
    header,
    text=(
        "Complete la información y responda las preguntas "
        "para generar la búsqueda documental"
    ),
    font=("Arial", 10),
    bg=COLOR_AZUL_OSCURO,
    fg="#DCEBFA"
)

subtitulo_principal.pack()


# ============================================================
# CONTENEDOR PRINCIPAL
# ============================================================

contenedor_principal = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

contenedor_principal.pack(
    fill="both",
    expand=True
)


canvas = tk.Canvas(
    contenedor_principal,
    bg=COLOR_FONDO,
    highlightthickness=0
)


scrollbar = tk.Scrollbar(
    contenedor_principal,
    orient="vertical",
    command=canvas.yview
)


canvas.configure(
    yscrollcommand=scrollbar.set
)


scrollbar.pack(
    side="right",
    fill="y"
)


canvas.pack(
    side="left",
    fill="both",
    expand=True
)


# ============================================================
# FORMULARIO
# ============================================================

frame_formulario = tk.Frame(
    canvas,
    bg=COLOR_FONDO
)


canvas_window = canvas.create_window(
    (0, 0),
    window=frame_formulario,
    anchor="n"
)


# ============================================================
# AJUSTAR ANCHO
# ============================================================

def ajustar_ancho(event):

    canvas.itemconfig(
        canvas_window,
        width=event.width
    )


canvas.bind(
    "<Configure>",
    ajustar_ancho
)


# ============================================================
# ACTUALIZAR SCROLL
# ============================================================

def actualizar_scroll(event):

    canvas.configure(
        scrollregion=canvas.bbox("all")
    )


frame_formulario.bind(
    "<Configure>",
    actualizar_scroll
)


# ============================================================
# TARJETA DE INFORMACIÓN
# ============================================================

tarjeta_info = tk.Frame(
    frame_formulario,
    bg=COLOR_TARJETA,
    highlightthickness=1,
    highlightbackground=COLOR_BORDE
)


tarjeta_info.pack(
    padx=80,
    pady=25,
    ipadx=30,
    ipady=20
)


# ============================================================
# NOMBRE DE LA INICIATIVA
# ============================================================

label_nombre = tk.Label(
    tarjeta_info,
    text="Nombre de la iniciativa, producto, servicio, proceso o tema",
    font=("Arial", 11, "bold"),
    bg=COLOR_TARJETA,
    fg=COLOR_TEXTO
)

label_nombre.pack(
    pady=(5, 5)
)


entrada_nombre = tk.Entry(
    tarjeta_info,
    font=("Arial", 11),
    width=75,
    justify="center",
    bg="#F8FAFC",
    fg=COLOR_TEXTO,
    relief="flat",
    highlightthickness=1,
    highlightbackground=COLOR_BORDE,
    highlightcolor=COLOR_AZUL
)

entrada_nombre.pack(
    ipady=8,
    pady=(0, 18)
)


# ============================================================
# SUB PROCESO
# ============================================================

label_subproceso = tk.Label(
    tarjeta_info,
    text="Sub Proceso objetivo",
    font=("Arial", 11, "bold"),
    bg=COLOR_TARJETA,
    fg=COLOR_TEXTO
)

label_subproceso.pack(
    pady=(0, 5)
)


entrada_subproceso = tk.Entry(
    tarjeta_info,
    font=("Arial", 11),
    width=75,
    justify="center",
    bg="#F8FAFC",
    fg=COLOR_TEXTO,
    relief="flat",
    highlightthickness=1,
    highlightbackground=COLOR_BORDE,
    highlightcolor=COLOR_AZUL
)

entrada_subproceso.pack(
    ipady=8
)


# ============================================================
# TÍTULO DE PREGUNTAS
# ============================================================

titulo_preguntas = tk.Label(
    frame_formulario,
    text="Preguntas de evaluación",
    font=("Arial", 16, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)

titulo_preguntas.pack(
    pady=(5, 5)
)


descripcion_preguntas = tk.Label(
    frame_formulario,
    text="Seleccione Sí o No en cada pregunta.",
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO_SECUNDARIO
)

descripcion_preguntas.pack(
    pady=(0, 15)
)


# ============================================================
# PREGUNTAS 3 A 12
# ============================================================

for i, item in enumerate(
    preguntas_documentos
):

    numero_pregunta = i + 3

    tarjeta = tk.Frame(
        frame_formulario,
        bg=COLOR_TARJETA,
        highlightthickness=1,
        highlightbackground=COLOR_BORDE
    )

    tarjeta.pack(
        padx=80,
        pady=7,
        ipadx=25,
        ipady=15
    )

    # --------------------------------------------------------
    # NÚMERO
    # --------------------------------------------------------

    numero = tk.Label(
        tarjeta,
        text=f"{numero_pregunta}",
        font=("Arial", 10, "bold"),
        bg=COLOR_AZUL_CLARO,
        fg=COLOR_AZUL,
        width=4
    )

    numero.pack(
        pady=(0, 8)
    )

    # --------------------------------------------------------
    # PREGUNTA
    # --------------------------------------------------------

    label_pregunta = tk.Label(
        tarjeta,
        text=item["pregunta"],
        font=("Arial", 11),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO,
        wraplength=720,
        justify="center"
    )

    label_pregunta.pack(
        padx=20,
        pady=(0, 12)
    )

    # --------------------------------------------------------
    # VARIABLE
    # --------------------------------------------------------

    respuesta = tk.StringVar(
        value=""
    )

    respuestas_si_no.append(
        respuesta
    )

    # --------------------------------------------------------
    # OPCIONES
    # --------------------------------------------------------

    opciones = tk.Frame(
        tarjeta,
        bg=COLOR_TARJETA
    )

    opciones.pack()

    radio_si = tk.Radiobutton(
        opciones,
        text="Sí",
        variable=respuesta,
        value="Sí",
        font=("Arial", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO,
        activebackground=COLOR_TARJETA,
        activeforeground=COLOR_AZUL,
        selectcolor=COLOR_AZUL_CLARO,
        cursor="hand2"
    )

    radio_si.pack(
        side="left",
        padx=25
    )

    radio_no = tk.Radiobutton(
        opciones,
        text="No",
        variable=respuesta,
        value="No",
        font=("Arial", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO,
        activebackground=COLOR_TARJETA,
        activeforeground=COLOR_AZUL,
        selectcolor=COLOR_AZUL_CLARO,
        cursor="hand2"
    )

    radio_no.pack(
        side="left",
        padx=25
    )


# ============================================================
# BOTÓN CONTINUAR
# ============================================================

boton_aceptar = tk.Button(
    frame_formulario,
    text="Generar búsqueda",
    command=aceptar,
    font=("Arial", 12, "bold"),
    bg=COLOR_AZUL,
    fg=COLOR_BLANCO,
    activebackground=COLOR_AZUL_OSCURO,
    activeforeground=COLOR_BLANCO,
    relief="flat",
    bd=0,
    cursor="hand2",
    width=22,
    pady=12
)

boton_aceptar.pack(
    pady=30
)


# ============================================================
# PIE DE PÁGINA
# ============================================================

footer = tk.Label(
    frame_formulario,
    text="Todas las preguntas cerradas son obligatorias.",
    font=("Arial", 9),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO_SECUNDARIO
)

footer.pack(
    pady=(0, 30)
)


# ============================================================
# SCROLL CON RUEDA DEL MOUSE
# ============================================================

def mover_scroll(event):

    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all(
    "<MouseWheel>",
    mover_scroll
)


# ============================================================
# INICIAR APLICACIÓN
# ============================================================

ventana.mainloop()