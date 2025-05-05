import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Crear la ventana principal con temas
root = ThemedTk(theme="radiance")
root.title("Aplicación con Cambio de Temas")

# Temas que me gustan a mi: Breeze - Scidgreen - Elegance - xpnative - vista.

# Crear algunos widgets de ejemplo
ttk.Label(root, text="Hola, Tkinter con ttkthemes!").pack(pady=10)
ttk.Button(root, text="Presióname").pack(pady=10)

# Función para cambiar de tema
def cambiar_tema():
    tema_seleccionado = tema_var.get()
    root.set_theme(tema_seleccionado)

# Crear un menú desplegable para seleccionar temas
tema_var = tk.StringVar(value="radiance")
temas = root.get_themes()  # Obtener la lista de temas disponibles
menu_temas = ttk.OptionMenu(root, tema_var, *temas, command=lambda _: cambiar_tema())
menu_temas.pack(pady=10)

root.mainloop()




