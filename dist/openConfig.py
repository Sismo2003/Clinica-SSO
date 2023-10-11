import json
import tkinter as tkr
def loadpath(test):
    try:
        with open("config.json","r") as file:
            path = json.load(file);
            return  path.get(f'{test}')
    except:
        messagebox.showerror(message="Error al cargar la base de datos.",title="Carga de base de datos error")




def treeviewLoadData (treeview,toppinglist):
    try:
        with open("config.json","r") as file:
           path = json.load(file);
    except:
        messagebox.showerror(message="Error al cargar la base de datos.",title="Carga de base de datos error")
    try:
        with open(path.get("DatabasePath"), "r") as file:
            main = json.load(file)
        JsonList = main;
        list_value = [list(JsonList.values()) for JsonList in JsonList]
        for col_names in toppinglist:
            treeview.heading(col_names,text=col_names)

        for value_tuple in list_value[0:]:
            treeview.insert('',tkr.END,values=value_tuple)
    except:
        messagebox.showerror(message="Error al cargar la base de datos.",title="Carga de base de datos error")
        return True
        