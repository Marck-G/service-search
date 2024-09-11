from core import core_load_conf, odoo_host_search
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import threading
import sys, os

VERSION = "0.0.2"


CONF = core_load_conf()

URL = None

APP = CONF["core"]["searchApp"] if CONF["core"]["searchApp"] else "odoo"

def ruta_absoluta(relative_path):
    # Si está empaquetado por PyInstaller
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # Ruta temporal creada por PyInstaller
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def open_browser():
    print("URL:", URL)
    webbrowser.open(URL)

def open(host):
    global URL
    port = CONF["core"]["defaultPort"]
    URL = (f"http://{host}:{port}")

def search_process(barra, v, ipText):
    print("Hilo iniciado")
    print(CONF)
    host = CONF["core"]["hostMask"]
    port = CONF["core"]["defaultPort"]
    min = CONF["core"]["startIP"]
    print(f"data: port:{port} host: {host}")
    host = odoo_host_search(host, port, barra, v.update_idletasks, min, ipText)
    if host:
        open(host)
        # boton.config(state=tk.NORMAL)
        barra["value"] = 100
        v.update_idletasks()
        texto.config(text=f"{APP} en {host}")
        messagebox.showinfo("Encontrado", f"Se ha encontrado un {APP} en {host}")
        open_browser()
    else:
        messagebox.showerror("Error", f"No se ha podido encontrar {APP} en la red")

ventana = tk.Tk()
ventana.title(f"Katalyst {APP} Finder")

ventana.geometry("300x100")
red = CONF["core"]["hostMask"].replace("X", "0")
texto = ttk.Label(ventana,text=f"Iniciada la busqueda en la red: {red}")
texto.pack(pady=4)

barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate")
barra_progreso.pack(pady=2)

ip = ttk.Label(ventana, text="")
ip.pack( pady=2)

help = ttk.Label(ventana,font=("Arial", 8), text="Se abrirá de forma automática en el navegador")
help.pack( pady=2)

# Creación de un botón deshabilitado inicialmente
# boton = ttk.Button(ventana, text="Abrir Odoo", state=tk.DISABLED, command=open_browser)
# boton.pack(pady=5)

icon = tk.PhotoImage(file=ruta_absoluta("assets/icon_64.png"))
ventana.iconphoto(False, icon)

hilo = threading.Thread(target=search_process, args=(barra_progreso, ventana, ip))
hilo.start()
ventana.mainloop()

