import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

def seleccionar_opcion(event):
    global selected_option
    selected_option = option_combobox.get()

def seleccionar_directorio():
    global selected_directory
    selected_directory = filedialog.askdirectory()

def buscar():
    global selected_option
    global selected_directory
    count = 0
    if selected_directory is None:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Por favor selecciona un directorio.")
        return
    with open("BBDD.txt", "r") as f:
        for line in f:
            line_parts = line.strip().split("=")
            if line_parts[0] == selected_option:
                search_string = line_parts[1]
                break
    for filename in os.listdir(selected_directory):
        if filename.endswith(".json"):
            with open(os.path.join(selected_directory, filename), "r") as f:
                content = f.read()
                if search_string in content:
                    count += 1
    result_text.delete('1.0', tk.END)
    result_text.tag_configure("center", justify='center')  # Añadir tag 'center' con el método justify como 'center'
    result_text.insert(tk.END, f"\nSe encontraron {count} eventos.", 'center')


root = tk.Tk()
root.title("JSON's Seek")
root.geometry("315x220")
root.eval("tk::PlaceWindow . center")

# Establecer el icono de la pluma
root.iconbitmap('./json.ico')

# Establecer color de fondo de la ventana
root.configure(bg="gray16", pady=12)

# agregar un widget de etiqueta como subtítulo
subtitulo = tk.Label(root, bg="gray16", relief=tk.FLAT, font=("Comic Sans", 12, "bold"))
subtitulo.pack()

# crear una etiqueta separada para cada parte del subtítulo
parte1 = tk.Label(subtitulo, text="FK", fg="red", bg="gray16", font=("Comic Sans", 12, "bold"))
parte1.pack(side="left")
parte2 = tk.Label(subtitulo, text="{ JSON's Seek }", fg="white", bg="gray16", font=("Comic Sans", 12))
parte2.pack(side="right")

# ajustar el tamaño de la etiqueta principal para que se adapte a las partes del subtítulo
subtitulo.update()
subtitulo.config(width=subtitulo.winfo_width())

subtitulo_2 = tk.Label(root, text= "NP6/Flex Solution Factory", bg="gray16", fg="white", relief=tk.FLAT, font=("Comic Sans", 7))
subtitulo_2.pack()

options = []
with open("BBDD.txt", "r") as f:
    for line in f:
        line_parts = line.strip().split("=")
        options.append(line_parts[0])

selected_option = None
option_combobox = ttk.Combobox(root, values=options, state="readonly", width=20, height=25)
option_combobox.set("Seleccionar..")
option_combobox.bind("<<ComboboxSelected>>", seleccionar_opcion)
option_combobox.place(x=31, y=93)

select_directory_button = tk.Button(root, text="Seleccionar Directorio", command=seleccionar_directorio, width=35, pady=1.56, height=1, bg="gray23",fg="white", relief=tk.FLAT, highlightthickness=0, activebackground="gray20", activeforeground="white")
select_directory_button.place(x=31, y=60)

search_button = tk.Button(root, text="Buscar Eventos", command=buscar, width=14, pady=0, height=0, bg="gray23",fg="white", relief=tk.FLAT, highlightthickness=0, activebackground="gray20", activeforeground="white")
search_button.place(x=178, y=93)

result_text = tk.Text(root, height=3, width=36, font='Helvetica 10', bg="white", bd=1, relief="solid")
result_text.place(x=30, y=123)

root.mainloop()







