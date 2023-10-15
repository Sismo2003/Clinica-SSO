import json
import tkinter as tkr
import os
config_file = os.path.join(os.path.dirname(__file__), 'documents/config.json')
forest_dark_file = os.path.join(os.path.dirname(__file__), 'documents/forest-dark.tcl')
forest_light_file = os.path.join(os.path.dirname(__file__), 'documents/forest-light.tcl')
db_file = os.path.join(os.path.dirname(__file__), 'documents/DB.json')
image_path = os.path.join(os.path.dirname(__file__), 'documents/images/imagen1.png')


def loadpath(test):
    try:
        with open(config_file,"r") as file:
            path = json.load(file);
            return  path.get(f'{test}')
    except:
        messagebox.showerror(message="Error al cargar la base de datos.",title="Carga de base de datos error")



