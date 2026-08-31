import tkinter as tk
from tkinter import messagebox
import webbrowser


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
# LINK DE SHAREPOINT
# ============================================================

LINK_DOCUMENTOS = (
    "https://credibanco.sharepoint.com/:x:/g/gestiondocumental/"
    "ET0awZ9z6V1Gi6ldXZ-AHPIBL3ui_44-1-ptXvitXFenyg?e=CQ1WRR"
)


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
# ABRIR LISTADO DE DOCUMENTOS
# ============================================================

def abrir_listado_documentos():

    try:

        webbrowser.open(LINK_DOCUMENTOS)

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No fue posible abrir el listado de documentos.\n\n{error}",
            parent=ventana
        )


# ============================================================
# MOSTRAR DOCUMENTOS NECESARIOS PARA LA INICIATIVA
# ============================================================

def mostrar_documentos_necesarios():

    # --------------------------------------------------------
    # OBTENER INFORMACIÓN
    # --------------------------------------------------------

    nombre_iniciativa = entrada_nombre.get().strip()
    subproceso = entrada_subproceso.get().strip()

    # --------------------------------------------------------
    # VALIDAR NOMBRE
    # --------------------------------------------------------

    if not nombre_iniciativa:

        messagebox.showwarning(
            "Información pendiente",
            "Por favor ingresa el nombre de la iniciativa, producto, "
            "servicio, proceso o tema.",
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

    for i, variable in enumerate(respuestas_si_no):

        if variable.get() == "":

            messagebox.showwarning(
                "Respuesta pendiente",
                f"Por favor responde la pregunta {i + 3}.",
                parent=ventana
            )

            return

    # --------------------------------------------------------
    # OBTENER SOLO LAS CATEGORÍAS CON "SÍ"
    # --------------------------------------------------------

    categorias_requeridas = []

    for i, variable in enumerate(respuestas_si_no):

        if variable.get() == "Sí":

            categorias_requeridas.append(
                preguntas_documentos[i]["documento"]
            )

    # ========================================================
    # CREAR NUEVA VENTANA
    # ========================================================

    ventana_documentos = tk.Toplevel(ventana)

    ventana_documentos.title(
        "Documentos necesarios para la iniciativa"
    )

    ventana_documentos.geometry(
        "850x700"
    )

    ventana_documentos.minsize(
        700,
        600
    )

    ventana_documentos.configure(
        bg=COLOR_FONDO
    )

    ventana_documentos.transient(
        ventana
    )

    # ========================================================
    # ENCABEZADO
    # ========================================================

    encabezado = tk.Frame(
        ventana_documentos,
        bg=COLOR_AZUL_OSCURO,
        height=110
    )

    encabezado.pack(
        fill="x"
    )

    encabezado.pack_propagate(
        False
    )

    titulo = tk.Label(
        encabezado,
        text="Documentos necesarios para esta iniciativa",
        font=("Arial", 18, "bold"),
        bg=COLOR_AZUL_OSCURO,
        fg=COLOR_BLANCO
    )

    titulo.pack(
        pady=(20, 3)
    )

    subtitulo = tk.Label(
        encabezado,
        text="Resultado basado en las respuestas del cuestionario",
        font=("Arial", 10),
        bg=COLOR_AZUL_OSCURO,
        fg="#D9E8F8"
    )

    subtitulo.pack()

    # ========================================================
    # CONTENEDOR
    # ========================================================

    contenedor = tk.Frame(
        ventana_documentos,
        bg=COLOR_FONDO
    )

    contenedor.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    # ========================================================
    # INFORMACIÓN DE LA INICIATIVA
    # ========================================================

    tarjeta_info = tk.Frame(
        contenedor,
        bg=COLOR_TARJETA,
        highlightthickness=1,
        highlightbackground=COLOR_BORDE
    )

    tarjeta_info.pack(
        fill="x",
        pady=(0, 15)
    )

    label_iniciativa_titulo = tk.Label(
        tarjeta_info,
        text="Iniciativa / Tema",
        font=("Arial", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO_SECUNDARIO
    )

    label_iniciativa_titulo.pack(
        anchor="w",
        padx=20,
        pady=(15, 2)
    )

    label_iniciativa = tk.Label(
        tarjeta_info,
        text=nombre_iniciativa,
        font=("Arial", 12, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO
    )

    label_iniciativa.pack(
        anchor="w",
        padx=20,
        pady=(0, 10)
    )

    label_subproceso_titulo = tk.Label(
        tarjeta_info,
        text="Sub Proceso objetivo",
        font=("Arial", 10, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO_SECUNDARIO
    )

    label_subproceso_titulo.pack(
        anchor="w",
        padx=20,
        pady=(0, 2)
    )

    label_subproceso = tk.Label(
        tarjeta_info,
        text=subproceso,
        font=("Arial", 12, "bold"),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO
    )

    label_subproceso.pack(
        anchor="w",
        padx=20,
        pady=(0, 15)
    )

    # ========================================================
    # TÍTULO DOCUMENTOS
    # ========================================================

    titulo_documentos = tk.Label(
        contenedor,
        text="Documentos que necesitaría la iniciativa",
        font=("Arial", 14, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )

    titulo_documentos.pack(
        anchor="w",
        pady=(0, 10)
    )

    # ========================================================
    # ÁREA DE DOCUMENTOS
    # ========================================================

    marco_documentos = tk.Frame(
        contenedor,
        bg=COLOR_TARJETA,
        highlightthickness=1,
        highlightbackground=COLOR_BORDE
    )

    marco_documentos.pack(
        fill="both",
        expand=True
    )

    texto_documentos = tk.Text(
        marco_documentos,
        font=("Arial", 11),
        bg=COLOR_TARJETA,
        fg=COLOR_TEXTO,
        relief="flat",
        bd=0,
        wrap="word",
        padx=20,
        pady=20
    )

    texto_documentos.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar_documentos = tk.Scrollbar(
        marco_documentos,
        orient="vertical",
        command=texto_documentos.yview
    )

    scrollbar_documentos.pack(
        side="right",
        fill="y"
    )

    texto_documentos.configure(
        yscrollcommand=scrollbar_documentos.set
    )

    # ========================================================
    # MOSTRAR RESULTADO
    # ========================================================

    if categorias_requeridas:

        texto_documentos.insert(
            tk.END,
            "Según las respuestas marcadas como \"Sí\", "
            "los documentos que necesitaría esta iniciativa son:\n\n"
        )

        for i, documento in enumerate(
            categorias_requeridas,
            start=1
        ):

            texto_documentos.insert(
                tk.END,
                f"{i}. {documento}\n\n"
            )

    else:

        texto_documentos.insert(
            tk.END,
            "De acuerdo con las respuestas del cuestionario, "
            "no se identificaron documentos requeridos entre las "
            "categorías evaluadas."
        )

    texto_documentos.config(
        state="disabled"
    )

    # ========================================================
    # BOTONES
    # ========================================================

    botones = tk.Frame(
        ventana_documentos,
        bg=COLOR_FONDO
    )

    botones.pack(
        pady=(0, 20)
    )

    boton_cerrar = tk.Button(
        botones,
        text="Cerrar",
        command=ventana_documentos.destroy,
        font=("Arial", 10, "bold"),
        bg=COLOR_AZUL,
        fg=COLOR_BLANCO,
        activebackground=COLOR_AZUL_OSCURO,
        activeforeground=COLOR_BLANCO,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=25,
        pady=8
    )

    boton_cerrar.pack()


# ============================================================
# MOSTRAR RESULTADO DEL PROMPT
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
    # RESALTAR NOMBRE DE INICIATIVA EN AMARILLO
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
    # RESALTAR CATEGORÍAS SELECCIONADAS EN VERDE
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
    # VALIDAR NOMBRE
    # --------------------------------------------------------

    if not nombre_iniciativa:

        messagebox.showwarning(
            "Información pendiente",
            "Por favor ingresa el nombre de la iniciativa, producto, "
            "servicio, proceso o tema.",
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

    # ========================================================
    # OBTENER ÚNICAMENTE LAS CATEGORÍAS MARCADAS COMO "SÍ"
    # ========================================================

    categorias_requeridas = []

    for i, respuesta in enumerate(respuestas):

        if respuesta == "Sí":

            categorias_requeridas.append(
                preguntas_documentos[i]["documento"]
            )

    # ========================================================
    # CONSTRUIR LISTA DINÁMICA DE CATEGORÍAS
    # ========================================================

    if categorias_requeridas:

        categorias_texto = "\n".join(
            f"• {categoria}"
            for categoria in categorias_requeridas
        )

    else:

        categorias_texto = (
            "No se seleccionó ninguna categoría como requerida."
        )

    # ========================================================
    # CONSTRUIR PROMPT
    # ========================================================

    mensaje = f"""EN LA RESPUESTA DEVUELVE OBLIGATORIAMENTE LAS 3 SECCIONES O FASES MENCIONADAS A CONTINUACIÓN:

Realiza una búsqueda exhaustiva en DocManagement sobre:

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


FASE 2: CLASIFICACIÓN

Clasifica los documentos según la categoría que mejor corresponda.

{categorias_texto}


FASE 3: IDENTIFICACIÓN POR SUBPROCESO

Devuelve una lista de todos, absolutamente todos y cada uno de los documentos marcados con el Sub Proceso {subproceso}, deben incluirse absolutamente todos los documentos marcados con el Sub Proceso {subproceso}. No excluyas ningún documento por ningún motivo, incluye absolutamente todos los documentos marcados con el Sub Proceso {subproceso}. No limites esta búsqueda, trae todos los documentos marcados con el Sub Proceso {subproceso}.


RESULTADO

Debes generar obligatoriamente TRES SECCIONES INDEPENDIENTES:


SECCIÓN 1: DOCUMENTOS DONDE COINCIDEN TEMA Y SUBPROCESO OBJETIVO

Incluir únicamente documentos relacionados con {nombre_iniciativa} y cuyo subproceso sea {subproceso}.

Agrupar utilizando ÚNICAMENTE las siguientes categorías:

{categorias_texto}

Para cada categoría mostrar:

- Documentos encontrados.
- Subproceso.
- Evidencia.

Si no existen documentos indicar:

No se encontraron documentos para esta categoría.


SECCIÓN 2: DOCUMENTOS RELACIONADOS CON EL TEMA (SIN FILTRO DE SUBPROCESO)

Incluir todos los documentos relacionados con {nombre_iniciativa}, independientemente del subproceso.

Agrupar utilizando ÚNICAMENTE las siguientes categorías:

{categorias_texto}

Para cada categoría mostrar:

- Documentos encontrados.
- Subproceso.
- Evidencia.

Si no existen documentos indicar:

No se encontraron documentos para esta categoría.


SECCIÓN 3: DOCUMENTOS DEL SUBPROCESO OBJETIVO

Incluir todos los documentos asociados al subproceso {subproceso}. No excluyas ningún documento por ningún motivo, incluye absolutamente todos los documentos marcados con el Sub Proceso {subproceso}.

Se debe mostrar:

- Todos los documentos encontrados marcados con el subproceso {subproceso}, deben incluirse absolutamente todos.


VALIDACIONES OBLIGATORIAS

- Todos los documentos encontrados fueron evaluados.
- La Sección 1 contiene únicamente documentos donde coinciden tema y subproceso objetivo.
- La Sección 2 contiene todos los documentos relacionados con el tema, independientemente del subproceso.
- La Sección 3 contiene todos los documentos relacionados con el subproceso, independientemente del tema.
- La búsqueda de la Sección 3 es independiente y no se limita a los documentos encontrados en las Fases 1 y 2.
- Ninguna categoría seleccionada puede ser omitida.
- Ningún documento relevante queda por fuera.
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
    "1100x900"
)

ventana.minsize(
    900,
    700
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
    height=130
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
        "El objetivo de esta herramienta es optimizar y facilitar la búsqueda "
        "documental de las iniciativas registradas en DocManagement.\n\n"
        "Complete la información y responda las preguntas "
        "para consultar y gestionar la documentación."
    ),
    font=("Arial", 10),
    bg=COLOR_AZUL_OSCURO,
    fg="#DCEBFA",
    justify="center"  # Centra ambas frases. Cambia a "left" si prefieres alineado a la izquierda.
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
# INFORMACIÓN SOBRE LOS BOTONES
# ============================================================

titulo_opciones = tk.Label(
    frame_formulario,
    text="¿Qué deseas hacer?",
    font=("Arial", 16, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)

titulo_opciones.pack(
    pady=(25, 5)
)


descripcion_opciones = tk.Label(
    frame_formulario,
    text=(
        "Utiliza una de las siguientes opciones según lo que necesites consultar."
    ),
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO_SECUNDARIO
)

descripcion_opciones.pack(
    pady=(0, 15)
)


# ============================================================
# CONTENEDOR DE INFORMACIÓN DE BOTONES
# ============================================================

tarjetas_botones = tk.Frame(
    frame_formulario,
    bg=COLOR_FONDO
)

tarjetas_botones.pack(
    padx=50,
    fill="x"
)


# ============================================================
# INFORMACIÓN BOTÓN 1
# ============================================================

info_boton_1 = tk.Frame(
    tarjetas_botones,
    bg=COLOR_TARJETA,
    highlightthickness=1,
    highlightbackground=COLOR_BORDE,
    width=300,
    height=150
)

info_boton_1.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

info_boton_1.pack_propagate(
    False
)


titulo_info_1 = tk.Label(
    info_boton_1,
    text="Generar Prompt",
    font=("Arial", 11, "bold"),
    bg=COLOR_TARJETA,
    fg=COLOR_AZUL
)

titulo_info_1.pack(
    pady=(12, 5)
)


texto_info_1 = tk.Label(
    info_boton_1,
    text=(
        "Este botón permite generar el prompt de búsqueda listo "
        "para copiar y pegar en el chatbot del agente de DocManager "
        "y obtener la respuesta directamente del agente en el chat."
    ),
    font=("Arial", 9),
    bg=COLOR_TARJETA,
    fg=COLOR_TEXTO_SECUNDARIO,
    wraplength=280,
    justify="center"
)

texto_info_1.pack(
    padx=10
)


# ============================================================
# INFORMACIÓN BOTÓN 2
# ============================================================

info_boton_2 = tk.Frame(
    tarjetas_botones,
    bg=COLOR_TARJETA,
    highlightthickness=1,
    highlightbackground=COLOR_BORDE,
    width=300,
    height=150
)

info_boton_2.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

info_boton_2.pack_propagate(
    False
)


titulo_info_2 = tk.Label(
    info_boton_2,
    text="Listado de documentos",
    font=("Arial", 11, "bold"),
    bg=COLOR_TARJETA,
    fg=COLOR_AZUL
)

titulo_info_2.pack(
    pady=(12, 5)
)


texto_info_2 = tk.Label(
    info_boton_2,
    text=(
        "Este botón permite acceder a todo el listado de absolutamente "
        "todos los documentos disponibles en DocManagement, donde podrá "
        "filtrar por nombre, Sub Proceso, Proceso, Gerencia, etc."
    ),
    font=("Arial", 9),
    bg=COLOR_TARJETA,
    fg=COLOR_TEXTO_SECUNDARIO,
    wraplength=280,
    justify="center"
)

texto_info_2.pack(
    padx=10
)


# ============================================================
# INFORMACIÓN BOTÓN 3
# ============================================================

info_boton_3 = tk.Frame(
    tarjetas_botones,
    bg=COLOR_TARJETA,
    highlightthickness=1,
    highlightbackground=COLOR_BORDE,
    width=300,
    height=150
)

info_boton_3.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5
)

info_boton_3.pack_propagate(
    False
)


titulo_info_3 = tk.Label(
    info_boton_3,
    text="Documentos necesarios",
    font=("Arial", 11, "bold"),
    bg=COLOR_TARJETA,
    fg=COLOR_AZUL
)

titulo_info_3.pack(
    pady=(12, 5)
)


texto_info_3 = tk.Label(
    info_boton_3,
    text=(
        "Este botón le permite conocer todos los documentos que "
        "necesitaría tener esta iniciativa según las respuestas "
        "que marque en las preguntas del cuestionario."
    ),
    font=("Arial", 9),
    bg=COLOR_TARJETA,
    fg=COLOR_TEXTO_SECUNDARIO,
    wraplength=280,
    justify="center"
)

texto_info_3.pack(
    padx=10
)


# ============================================================
# BOTONES PRINCIPALES
# ============================================================

botones_principales = tk.Frame(
    frame_formulario,
    bg=COLOR_FONDO
)

botones_principales.pack(
    pady=20,
    padx=40,
    fill="x"
)


# ------------------------------------------------------------
# BOTÓN 1 - GENERAR PROMPT
# ------------------------------------------------------------

boton_aceptar = tk.Button(
    botones_principales,
    text="Generar Prompt de Búsqueda\npara el bot DocManager",
    command=aceptar,
    font=("Arial", 10, "bold"),
    bg=COLOR_AZUL,
    fg=COLOR_BLANCO,
    activebackground=COLOR_AZUL_OSCURO,
    activeforeground=COLOR_BLANCO,
    relief="flat",
    bd=0,
    cursor="hand2",
    width=30,
    height=3,
    wraplength=230,
    justify="center"
)

boton_aceptar.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)


# ------------------------------------------------------------
# BOTÓN 2 - LISTADO DOCUMENTOS
# ------------------------------------------------------------

boton_listado = tk.Button(
    botones_principales,
    text="Consulte el listado de todos los\ndocumentos que existen en DocManagement",
    command=abrir_listado_documentos,
    font=("Arial", 10, "bold"),
    bg=COLOR_AZUL_OSCURO,
    fg=COLOR_BLANCO,
    activebackground=COLOR_AZUL,
    activeforeground=COLOR_BLANCO,
    relief="flat",
    bd=0,
    cursor="hand2",
    width=30,
    height=3,
    wraplength=230,
    justify="center"
)

boton_listado.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)


# ------------------------------------------------------------
# BOTÓN 3 - DOCUMENTOS NECESARIOS
# ------------------------------------------------------------

boton_documentos_necesarios = tk.Button(
    botones_principales,
    text="¿Qué documentos necesitaría\npara esta iniciativa?",
    command=mostrar_documentos_necesarios,
    font=("Arial", 10, "bold"),
    bg="#2E7D32",
    fg=COLOR_BLANCO,
    activebackground="#1B5E20",
    activeforeground=COLOR_BLANCO,
    relief="flat",
    bd=0,
    cursor="hand2",
    width=30,
    height=3,
    wraplength=230,
    justify="center"
)

boton_documentos_necesarios.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
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