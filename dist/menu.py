import tkinter as tkr
import json
from tkinter import ttk
from screenColoscopia import formColoscopia
from settings import configs
from openConfig import loadpath


def theme_mode (interruptor,style):
    if interruptor.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

def menu():
    root = tkr.Tk();
    root.title("Clinica SSO");
    theme_style = ttk.Style(root);
    with open ('config.json', "r") as file:
        path = json.load(file); 
    
    root.tk.call("source","forest-light.tcl");
    root.tk.call("source", "forest-dark.tcl");
    Frame = ttk.Frame(root);
    theme_style.theme_use("forest-dark")
    Frame.pack();
    
    widgetImages = tkr.Frame(Frame)
    widgetImages.grid(row=0,column=0,padx=10,pady=10)
    sosImage = tkr.PhotoImage(file="images/imagen1.png")
    imageadjust = sosImage.subsample(3,3)
    lblbarberimg = tkr.Label(widgetImages,image= imageadjust)
    lblbarberimg.grid(row=0,column=0,sticky="news",padx=10,pady=10)

    

    widgetFrames = ttk.LabelFrame(Frame, text="Reportes");
    widgetFrames.grid(row=1,column=0,padx=20,pady=20);
    
    coloscopiaButton =  ttk.Button(widgetFrames, text="Coloscopia", command=formColoscopia)
    coloscopiaButton.grid(padx=20 ,pady=20, row=0 , column=0)
    
    
   
    
    
    
    configPath = ttk.Button(widgetFrames,text="Configuraciones",command=configs)
    configPath.grid(padx=20,pady=20,row=0,column=1)
    
    
    
    mode_switch = ttk.Checkbutton(widgetFrames,text="Apariencia",style="Switch",command=lambda: theme_mode(mode_switch,theme_style))
    mode_switch.grid(row=2,column=0,padx=20,pady=20,sticky="NEWS")
    root.iconphoto(False,tkr.PhotoImage(file='images/imagen1.png'))
    root.mainloop()

menu();
