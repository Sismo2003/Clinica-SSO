import tkinter as tkr
from tkinter import ttk
import json
from openConfig import loadpath
import os
config_file = os.path.join(os.path.dirname(__file__), 'config.json')
forest_dark_file = os.path.join(os.path.dirname(__file__), 'forest-dark.tcl')
forest_light_file = os.path.join(os.path.dirname(__file__), 'forest-light.tcl')
db_file = os.path.join(os.path.dirname(__file__), 'DB.json')
image_path = os.path.join(os.path.dirname(__file__), 'images', 'imagen1.png')



def configs():
    
    
    def updateScreen(i):
        if(i == 1):
            BDPathLabel.config(text=f"{loadpath('DatabasePath')}")
        elif(i==2):
            DocxDocumentPathLabel.config(text=f"{loadpath('DocxTemplatePath')}")
        elif(i==3):
            DocxTemplatePathLabel.config(text=f"{loadpath('DocxSaveDocument')}")




    def image_path(i):
        if(i == 1):
            where = "DatabasePath"
            info = "Base de datos"
        elif(i==2):
            where = "DocxSaveDocument"
            info = "Documento Word"
        elif(i==3):
            where = "DocxTemplatePath"
            info = "Template Docx"
        else:
            print("error")
        try:    
            file_path = tkr.filedialog.askopenfilename(title=f"Seleccionar path para {info}")
            mssgbox = tkr.messagebox.askquestion(title=f"Cambio de PATH {info}", message=f"Estas seguro que quieres cambiar la dirrecion de la {info}? ")
            if(mssgbox == "yes"):
                with open(config_file,"r") as file:
                    path = json.load(file);
                path[where]=file_path;
                with open("config.json","w") as file:
                        json.dump(path,file,indent=4)
                updateScreen(i)
            else:
                print('No changes')
        except:
            tkr.messagebox.showerror(message=f"Error al cambiar el path de {info}")
    root=tkr.Toplevel()
    root.title("Configuraciones")
    
    frame = ttk.Frame(root)
    frame.pack()
    
    mainLabelFrame = ttk.Frame(frame)
    mainLabelFrame.grid(padx=20,pady=20,row=0,column=0)
    
    DBPath = ttk.Button(mainLabelFrame,text="Base de Datos",command= lambda : image_path(1))
    DBPath.grid(padx=20,pady=20,row=0,column=0)
    
    BDPathLabel = ttk.Label(mainLabelFrame,text=f"{loadpath('DatabasePath')}")
    BDPathLabel.grid(row=0,column=1,padx=20,pady=20)
    
    DocxDocumentPath = ttk.Button(mainLabelFrame,text="Word File Path",command= lambda : image_path(2))
    DocxDocumentPath.grid(row=1,column=0,padx=20,pady=20)
    
    DocxDocumentPathLabel = ttk.Label(mainLabelFrame,text=f"{loadpath('DocxTemplatePath')}")
    DocxDocumentPathLabel.grid(row=1,column=1,padx=20,pady=20)
    
    DocxTemplatePath = ttk.Button(mainLabelFrame,text="Word Template Path",command= lambda : image_path(3))
    DocxTemplatePath.grid(row=2,column=0,padx=20,pady=20)

    
    DocxTemplatePathLabel = ttk.Label(mainLabelFrame,text=f"{loadpath('DocxSaveDocument')}")
    DocxTemplatePathLabel.grid(row=2,column=1,padx=20,pady=20)
    root.iconphoto(False,tkr.PhotoImage(file=image_path))
    root.mainloop()