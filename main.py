import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

class TimeEntry(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # Variables para almacenar la hora y los minutos
        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        
        # Entrada de horas
        self.hour_entry = tk.Entry(self, width=2, textvariable=self.hour_var)
        self.hour_entry.grid(row=0, column=0)
        
        # Separador de horas y minutos
        tk.Label(self, text=":").grid(row=0, column=1)
        
        # Entrada de minutos
        self.minute_entry = tk.Entry(self, width=2, textvariable=self.minute_var)
        self.minute_entry.grid(row=0, column=2)
        
        # Valida la entrada para asegurar que solo se ingresen números y se limita el rango de horas y minutos
        self.hour_entry.config(validate="key", validatecommand=(self.register(self.validate_time), "%P", "%d", "hour"))
        self.minute_entry.config(validate="key", validatecommand=(self.register(self.validate_time), "%P", "%d", "minute"))
        
    def validate_time(self, new_value, action, field):
        if action == "1":  # Insertar
            if new_value.isdigit():
                if len(new_value) == 1:
                    # Agregar un cero delante si solo se ingresa un dígito
                    new_value = "0" + new_value
                if field == "hour":
                    return len(new_value) == 2 and int(new_value) <= 23
                elif field == "minute":
                    return len(new_value) == 2 and int(new_value) <= 59
            return False
        return True

def login(event=None):
    # Verifica si la contraseña ingresada es correcta
    if entry_password.get() == "pass":
        messagebox.showinfo("Login Exitoso", "Acceso concedido")
        # Cierra la ventana de inicio de sesión
        root.destroy()
        # Abre la ventana del menú principal
        abrir_menu_principal()
    else:
        messagebox.showerror("Error", "Contraseña incorrecta")

def abrir_menu_principal():
    # Configuración de la ventana del menú principal con temas
    menu_principal = ThemedTk(theme="vista")  # Cambia "radiance" al tema que prefieras
    menu_principal.title("Menú Principal")
    menu_principal.geometry("675x700")  # Ajusta el tamaño de la ventana
    menu_principal.resizable(False, False)  # Deshabilita la maximización de la ventana
    menu_principal.config(bg="#212121")  # Establece el color de fondo al mismo que el del login
    
    # Colores de fondo y texto para los Checkbuttons
    checkbutton_bg = "#212121"  # Color de fondo original
    checkbutton_fg = "white"    # Color de texto original

    # Crear los Checkbuttons con los colores ajustados
    checkbutton1 = tk.Checkbutton(menu_principal, text="Informe 1", bg=checkbutton_bg, fg=checkbutton_fg, selectcolor="gray")
    checkbutton1.place(x=30, y=40)

    checkbutton2 = tk.Checkbutton(menu_principal, text="Informe 2", bg=checkbutton_bg, fg=checkbutton_fg, selectcolor="gray")
    checkbutton2.place(x=30, y=90)

    checkbutton3 = tk.Checkbutton(menu_principal, text="Informe 3", bg=checkbutton_bg, fg=checkbutton_fg, selectcolor="gray")
    checkbutton3.place(x=30, y=140)


    # Etiqueta para la lista de emails
    label_email_list = tk.Label(menu_principal, text="Lista de Emails:", font=("Helvetica", 10, "bold"), bg="#212121", fg="white")
    label_email_list.place(x=150, y=20)

    # Lista de emails
    email_listbox = tk.Listbox(menu_principal)
    email_listbox.place(x=150, y=40, width=200, height=150)
    
    scrollbar = tk.Scrollbar(menu_principal, orient="vertical", command=email_listbox.yview)
    email_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.place(x=350, y=40, height=150)

    # Entrada para nuevo email con placeholder
    entry_email = tk.Entry(menu_principal)
    entry_email.place(x=150, y=200, width=200)
    
    placeholder_text = "Agregar o quitar Emails"

    def clear_placeholder(event=None):
        if entry_email.get() == placeholder_text:
            entry_email.delete(0, tk.END)
            entry_email.config(fg='black')

    def on_focusout(event):
        if entry_email.get() == '':
            entry_email.insert(0, placeholder_text)
            entry_email.config(fg='grey')

    entry_email.insert(0, placeholder_text)
    entry_email.bind('<FocusIn>', clear_placeholder)
    entry_email.bind('<FocusOut>', on_focusout)
    entry_email.config(fg='grey')

    # Función para agregar email
    def agregar_email():
        clear_placeholder()
        email = entry_email.get()
        if email and email!= placeholder_text:
            email_listbox.insert(tk.END, email)
            entry_email.delete(0, tk.END)
            entry_email.insert(0, placeholder_text)
            entry_email.config(fg='grey')

    # Función para quitar email
    def quitar_email():
        clear_placeholder()
        selected = email_listbox.curselection()
        if selected:
            email_listbox.delete(selected)

    # Botón para agregar email
    button_agregar = tk.Button(menu_principal, text="Agregar", command=agregar_email, bg="#0193bd", fg="white")
    button_agregar.place(x=190, y=230)

    # Botón para quitar email
    button_quitar = tk.Button(menu_principal, text="Quitar", command=quitar_email, bg="#0193bd", fg="white")
    button_quitar.place(x=260, y=230)

    # Etiqueta para la vista previa
    label_vista_previa = tk.Label(menu_principal, text="Vista Previa:", font=("Helvetica", 10, "bold"), bg="#212121", fg="white")
    label_vista_previa.place(x=50, y=280)

    # Lienzo para mostrar la imagen
    canvas = tk.Canvas(menu_principal, width=300, height=375, bg="white")
    canvas.place(x=50, y=300)

    # Cargar la imagen y redimensionarla
    try:
        original_image = Image.open("./assets/screenshot.png")
        resized_image = original_image.resize((300, 375), Image.BICUBIC)  # Ajusta el tamaño según tu lienzo
        image = ImageTk.PhotoImage(resized_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
    except Exception as e:
        print(f"Error al cargar o redimensionar la imagen: {e}")
    
    # Etiqueta para el cronograma de envío
    label_cronograma = tk.Label(menu_principal, text="Cronograma de envío:", font=("Helvetica", 10, "bold"), bg="#212121", fg="white")
    label_cronograma.place(x=400, y=20)

    # Etiqueta para fecha específica
    label_fecha_especifica = tk.Label(menu_principal, text="Fecha específica:", bg="#212121", fg="white")
    label_fecha_especifica.place(x=400, y=55)

    # Input de calendario para seleccionar una fecha
    date_entry = DateEntry(menu_principal, width=15, background='#5f5f5f',
                           foreground='white', borderwidth=2, year=2024, month=6, day=1)
    date_entry.place(x=403, y=75)

    # Etiqueta para días de la semana
    label_dias_semana = tk.Label(menu_principal, text="Días de la semana:", bg="#212121", fg="white")
    label_dias_semana.place(x=400, y=110)

    # Colores de fondo y texto para los Checkbuttons de días de la semana
    checkbutton_bg = "#212121"  # Color de fondo original
    checkbutton_fg = "white"    # Color de texto original

    # Crear los Checkbuttons con los colores ajustados para los días de la semana
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    x_position = 400
    y_position = 130
    for dia in dias_semana:
        checkbutton = tk.Checkbutton(menu_principal, text=dia, bg=checkbutton_bg, fg=checkbutton_fg, selectcolor="gray")
        checkbutton.place(x=x_position, y=y_position)
        y_position += 30

        
    # Agregar etiqueta para el horario
    label_horario = tk.Label(menu_principal, text="Horario:", font=("Helvetica", 10), bg="#212121", fg="white")
    label_horario.place(x=400, y=353)  # Ajusta la posición según tu diseño
    
    # Agregar TimeEntry para seleccionar la hora
    time_entry = TimeEntry(menu_principal, width=5)  # Ajusta el ancho según tu diseño
    time_entry.place(x=403, y=378)  # Ajusta la posición según tu diseño
    
    # Agregar botón "Programar envío"
    button_programar_envio = tk.Button(menu_principal, text="Programar envío", command=lambda: print("Programar envío"),bg="#0193bd", fg="white")
    button_programar_envio.place(x=400, y=440)

    # Agregar botón "Enviar Reporte ahora"
    button_enviar_reporte = tk.Button(menu_principal, text="Enviar Reporte ahora", command=lambda: print("Enviar Reporte ahora"), bg="#0193bd", fg="white")
    button_enviar_reporte.place(x=400, y=480)

    menu_principal.mainloop()

# Configuración de la ventana Login con tema
root = ThemedTk(theme="vista")  # Cambia "radiance" al tema que prefieras
root.title("Login")
root.geometry("350x150")  # Establece el ancho y alto de la ventana
root.resizable(False, False)  # Deshabilita la maximización de la ventana
root.config(bg="#212121")

# Resto del código para la ventana de login
label_password = tk.Label(root, text="Contraseña:", bg="#212121", fg="white")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(root, text="Login", command=login, bg="#0193bd", fg="white")
button_login.pack(pady=10)

# Vincula la tecla Enter para el evento de login
root.bind('<Return>', login)

root.mainloop()