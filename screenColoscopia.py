import tkinter as tkr
import json
from tkinter import ttk
import calendar
from tkcalendar import DateEntry 
from tkinter import scrolledtext, filedialog
from docCreate import createDocument
import os
from openConfig import folioLoad
config_file = os.path.join(os.path.dirname(__file__), 'config.json')
forest_dark_file = os.path.join(os.path.dirname(__file__), 'forest-dark.tcl')
forest_light_file = os.path.join(os.path.dirname(__file__), 'forest-light.tcl')
db_file = os.path.join(os.path.dirname(__file__), 'DB.json')
image_path = os.path.join(os.path.dirname(__file__), 'documents/imagen1.png')



def formColoscopia():
    def submission():
        nonlocal ImagesStrPaths
        fullNamestr = fullNameEntry.get()
        fullNamestr = fullNamestr.title()
        pregnanciesstr = pregnanciesEntry.get()
        clientAgeEntrystr = clientAgeEntry.get()
        MedicToEntrystr = MedicToEntry.get()
        MedicToEntrystr = MedicToEntrystr.capitalize()
        dateofExamsEntrystr = dateofExamsEntry.get()
        birthsEntrystr = birthsEntry.get()
        abortionEntrystr = abortionEntry.get()
        fumFinalResultstr= fumFinalResult.get()
        cSectionEntrystr = cSectionEntry.get()
        vaginaVulvaEntrystr = vaginaVulvaEntry.get('1.0', tkr.END)
        vaginaVulvaEntrystr.capitalize()
        cervixEntrystr = cervixEntry.get()
        patronVascularEntrystr = patronVascularEntry.get()
        patronVascularEntrystr = patronVascularEntrystr.capitalize()
        zonaDeTransformacionEntrystr = zonaDeTransformacionEntry.get()
        unionEscamocilindricaEntrystr = unionEscamocilindricaEntry.get()
        epitelioEscamosoEntrystr = epitelioEscamosoEntry.get()
        EpitelioCilindricoEntrystr = EpitelioCilindricoEntry.get()
        TestDeHinselmaEntrystr = TestDeHinselmaEntry.get()
        TestDeScillerEntrystr = TestDeScillerEntry.get()
        ColposcopiaQuestionEntrystr = ColposcopiaQuestionEntry.get()
        hallazgosColposcopicosEntrystr = hallazgosColposcopicosEntry.get('1.0', tkr.END)
        hallazgosColposcopicosEntrystr = hallazgosColposcopicosEntrystr.capitalize()
        comtPlanTerapeuticoEntrystr = comtPlanTerapeuticoEntry.get('1.0', tkr.END)
        comtPlanTerapeuticoEntrystr = comtPlanTerapeuticoEntrystr.capitalize()
        doctor1NameEntrystr = doctor1NameEntry.get()
        doctor1NameEntrystr = doctor1NameEntrystr.title()
        cedProfEntrystr = cedProfEntry.get()
        diagnosticoColposcopico = diagnosticoColposcopicoEntry.get()
        images= []

        for i in ImagesStrPaths:
            if(i != ""):
                images.append(i.get())
      
        if(fullNamestr == "" or dateofExamsEntrystr == "" or MedicToEntrystr == "" or clientAgeEntrystr == "" or pregnanciesstr == ""
           or birthsEntrystr == "" or cSectionEntrystr == "" or cervixEntrystr == "Selecciona" or patronVascularEntrystr == "Selecciona" or zonaDeTransformacionEntrystr == "Selecciona"
           or unionEscamocilindricaEntry == "Selecciona" or epitelioEscamosoEntrystr == "Selecciona" or EpitelioCilindricoEntrystr == "Selecciona" or TestDeHinselmaEntrystr == "Selecciona"
           or TestDeScillerEntrystr == "Selecciona" or ColposcopiaQuestionEntrystr == "Selecciona" or diagnosticoColposcopico == "Selecciona" or diagnosticoColposcopico == ""
           ):
            tkr.messagebox.showwarning(title="Campos vacios",message="Faltan campos por llenar, favor de revisar.")
        
        else:
            question = createDocument(fullNamestr,pregnanciesstr,clientAgeEntrystr,MedicToEntrystr,dateofExamsEntrystr,birthsEntrystr,abortionEntrystr,
                fumFinalResultstr,cSectionEntrystr,vaginaVulvaEntrystr,cervixEntrystr,patronVascularEntrystr,zonaDeTransformacionEntrystr,
                unionEscamocilindricaEntrystr,epitelioEscamosoEntrystr,EpitelioCilindricoEntrystr,TestDeHinselmaEntrystr,TestDeScillerEntrystr,
                ColposcopiaQuestionEntrystr,hallazgosColposcopicosEntrystr,comtPlanTerapeuticoEntrystr,doctor1NameEntrystr,cedProfEntrystr,
                diagnosticoColposcopico,images
            )
            if(question): 
                    window.destroy()

            

    
        
    window = tkr.Toplevel()
    window.title("Formulario Coloscopia")
    frame = ttk.Frame(window)
    frame.pack()
    
        ####################### Informacion del Cliente#####################
    clientInfo = ttk.LabelFrame(frame,text="Informacion del Cliente")
    clientInfo.grid(row=0, column=0, padx=10 ,pady=10)
    
    fullNameLabel = ttk.Label(clientInfo,text="PACIENTE:") # columa 0 y 1
    fullNameEntry = ttk.Entry(clientInfo)
    fullNameLabel.grid(row=0,column=0,pady=0, columnspan=2, sticky="n");
    fullNameEntry.grid(row=1,column=0,padx=5, pady=5,columnspan=2,sticky="nsew");
    
    DateOfExamfinal_result = tkr.StringVar()
    dateOfExamsLabel = ttk.Label(clientInfo,text="FECHA DE ESTUDIO:")
    dateofExamsEntry = DateEntry(clientInfo,selectmode="day",textvariable=DateOfExamfinal_result)
    dateOfExamsLabel.grid(row= 0 ,column=3 ,sticky="NEWS" ,padx=20,pady=5)
    dateofExamsEntry.grid(row=1, column= 3, padx=10,pady=5)
       
    
    MedicToLabel = ttk.Label(clientInfo,text="MEDICO A QUIEN VA DIRIJIDO EL ESTUDIO: ")
    MedicToEntry = ttk.Entry(clientInfo)
    MedicToLabel.grid(row=2,column=0, padx=10, pady=5)
    MedicToEntry.grid(row=3,column=0, padx=20,pady=5)
    
    
    clientAgeLabel = ttk.Label(clientInfo,text="EDAD:")
    clientAgeEntry = ttk.Spinbox(clientInfo,from_=0 , to=100)
    clientAgeLabel.grid(row=2,column=1,padx=10)
    clientAgeEntry.grid(row=3,column=1, padx=10)
    
    
    FolioLabel = ttk.Label(clientInfo,text="Folio:")
    FolioEntry = ttk.Label(clientInfo,text=f"{folioLoad('folio')} ")
    FolioLabel.grid(row=2, column=3, padx=10);
    FolioEntry.grid(row=3,column=3, padx=10);
    
    ####################### DATOS GINECO OBSTÉTRICOS #####################
    Gineco = ttk.LabelFrame(frame,text="DATOS GINECO OBSTÉTRICOS")
    Gineco.grid(row=0, column=1, padx=10 ,pady=10)#, padx=10 ,pady=10
        
    pregnanciesLabel = ttk.Label(Gineco,text="EMBARAZOS:");
    pregnanciesEntry= ttk.Spinbox(Gineco,from_=0 , to=100);
    pregnanciesLabel.grid(row=0,column=0,padx=5,pady=5)
    pregnanciesEntry.grid(row=1,column=0,padx=10,pady=5)
    
    
    
    birthsLabel = ttk.Label(Gineco,text="PARTOS:")
    birthsEntry = ttk.Spinbox(Gineco,from_=0 , to=100)
    birthsLabel.grid(row=0, column=1, padx=5,pady=5)
    birthsEntry.grid(row=1,column=1,padx=10,pady=5)
    
    abortionLabel = ttk.Label(Gineco,text="ABORTOS:")
    abortionEntry = ttk.Spinbox(Gineco,from_=0 , to=100)
    abortionLabel.grid(row=3,column=1,padx=10,pady=5)
    abortionEntry.grid(row=4,column=1,padx=10,pady=5)
    
    fumFinalResult = tkr.StringVar()
    fumLabel = ttk.Label(Gineco,text="FUM:")
    fumEntry = DateEntry(Gineco,selectmode="day",textvariable=fumFinalResult)
    fumLabel.grid(row=0,column=2,padx=10,pady=5)
    fumEntry.grid(row=1,column=2,padx=10,pady=5)
    
    
    cSectionLabel = ttk.Label(Gineco,text="CESÁREAS:")
    cSectionEntry = ttk.Spinbox(Gineco,from_=0 , to=100) 
    cSectionLabel.grid(row=3,column=0,padx=10,pady=5)
    cSectionEntry.grid(row=4,column=0,padx=10,pady=5)
    
    ####################### colposcopicFrame #####################
        
    colposcopicFrame = ttk.Labelframe(frame,text="DATOS COLPOSCOPICOS")
    colposcopicFrame.grid(row=1,column=1, padx=10 ,pady=10) #padx = 10 ,pady=5
    
    vaginaVulvaLabel = ttk.Label(colposcopicFrame,text="VULVA Y VAGINA:")
    vaginaVulvaEntry = tkr.scrolledtext.ScrolledText(colposcopicFrame,height=5,width=60, font=("Arial",15), highlightbackground="#272727", highlightcolor="#272727")
    vaginaVulvaLabel.grid(row=0,column=0,padx=10,pady=5,columnspan=3,sticky="N")
    vaginaVulvaEntry.grid(row=1,column=0,padx=10,pady=5,columnspan=3)
    
    
    cervixLabel = ttk.Label(colposcopicFrame,text="CERVIX:")
    cervixEntry = ttk.Combobox(colposcopicFrame)
    cervixEntry['values']=("Seleccione","EUTROFICO", "HIPERTROFICO"," ATROFICO"," CUPULIZADO")
    cervixEntry.current(0)
    cervixLabel.grid(row=3,column=0,padx=10,pady=5)
    cervixEntry.grid(row=4,column=0,padx=10,pady=5)
    
    
    
    patronVascularLabel = ttk.Label(colposcopicFrame,text="PATRON VASCULAR (ARAGONÉS):")
    patronVascularEntry = ttk.Combobox(colposcopicFrame)
    patronVascularEntry['values']=("Seleccione","Tipo I Normal: Fina red capilar (arboriforme)" , "Tipo II aumentado: aumento de la red normal Imagen vascular de colpitis", "Tipo III Ectásico: Vasos Dilatados Distribución normal Tipo IV irregular: Horquillas, sacacorchos. Cambios bruscos de dirección ", "Tipo V atípico: Dilataciones y estenosis Interrupciones bruscas")
    patronVascularEntry.current(0)
    patronVascularLabel.grid(row=3,column=1,padx=10,pady=5)
    patronVascularEntry.grid(row=4,column=1,padx=10,pady=5)
    
    
    zonaDeTransformacionLabel = ttk.Label(colposcopicFrame,text="ZONA DE TRANSFORMACION:")
    zonaDeTransformacionEntry = ttk.Combobox(colposcopicFrame)
    zonaDeTransformacionEntry['values']=("Selecciona","TIPO 1 EXOCERVICAL", "TIPO 2 ELEMENTOS DE LA ZT", "QUE SE INTRODUCEN A CANAL ENDOCERVICAL")
    zonaDeTransformacionEntry.current(0)
    zonaDeTransformacionLabel.grid(row=3,column=2,padx=10,pady=5 )
    zonaDeTransformacionEntry.grid(row=4,column=2,padx=10,pady=5)
    
    unionEscamocilindricaLabel = ttk.Label(colposcopicFrame,text="UNION ESCAMOCILINDRICA:")
    unionEscamocilindricaEntry = ttk.Combobox(colposcopicFrame)
    unionEscamocilindricaEntry['values']=("Selecciona","visible", " Parcialmente visible " ,"No visible.")
    unionEscamocilindricaEntry.current(0)
    unionEscamocilindricaLabel.grid(row=5,column=0,padx=10,pady=5)
    unionEscamocilindricaEntry.grid(row=6,column=0, padx=10,pady=5)
    
    
    
    epitelioEscamosoLabel = ttk.Label(colposcopicFrame,text="EPITELIO ESCAMOSO:")
    epitelioEscamosoEntry = ttk.Combobox(colposcopicFrame)
    epitelioEscamosoEntry['values']=("Selecciona","Maduro"," Atrófico")
    epitelioEscamosoEntry.current(0)
    epitelioEscamosoLabel.grid(row=5,column=1,padx=10,pady=5)
    epitelioEscamosoEntry.grid(row=6,column=1,padx=10,pady=5)
    

    
    EpitelioCilindricoLabel = ttk.Label(colposcopicFrame,text="EPITELIO CILINDRICO")
    EpitelioCilindricoEntry = ttk.Combobox(colposcopicFrame)
    EpitelioCilindricoEntry['values']=("Selecciona", "Con ectopia","Sin ectopia")
    EpitelioCilindricoEntry.current(0)
    EpitelioCilindricoLabel.grid(padx=10,pady=5,row=5, column=2)
    EpitelioCilindricoEntry.grid(padx=10,pady=5,row=6,column=2)    
    
    
    
    TestDeHinselmaLabel = ttk.Label(colposcopicFrame,text="TEST DE HINSELMAN (ACETICO):")
    TestDeHinselmaEntry = ttk.Combobox(colposcopicFrame)
    TestDeHinselmaEntry['values']= ("Selecciona","Positivo" ,"Negativo")
    TestDeHinselmaEntry.current(0)
    TestDeHinselmaLabel.grid(padx=10,pady=5,row=7,column=0)
    TestDeHinselmaEntry.grid(padx=10,pady=5,row=8, column=0)
    
    
    TestDeScillerLabel = ttk.Label(colposcopicFrame,text="TEST DE SCHILLER:")
    TestDeScillerEntry = ttk.Combobox(colposcopicFrame)
    TestDeScillerEntry['values']= ("Selecciona","Positivo" ,"Negativo")
    TestDeScillerEntry.current(0)
    TestDeScillerLabel.grid(padx=10,pady=5,row=7, column=1)
    TestDeScillerEntry.grid(padx=10,pady=5,row=8,column=1)
    
    
    ColposcopiaQuestionLabel = ttk.Label(colposcopicFrame,text="COLPOSCOPIA:")
    ColposcopiaQuestionEntry = ttk.Combobox(colposcopicFrame)
    ColposcopiaQuestionEntry['values']= ("Selecciona","ADECUADA" ,"NO ADECUADA")
    ColposcopiaQuestionEntry.current(0);
    ColposcopiaQuestionLabel.grid(padx=10,pady=5,row=7,column=2)
    ColposcopiaQuestionEntry.grid(padx=10,pady=5,row=8,column=2)
    
    

    
    
    
    ######### HALLASZGOS COLPOSCOPICOS ANORMALES:###############
    
    coloscopicDataFrame2 = ttk.LabelFrame(frame,text="DATOS COLPOSCOPICOS:")
    coloscopicDataFrame2.grid(row=1,column=0,padx=10,pady=5,rowspan=2)
    
    
    
    hallazgosColposcopicosLabel = ttk.Label(coloscopicDataFrame2,text="HALLASZGOS COLPOSCOPICOS ANORMALES:")
    hallazgosColposcopicosEntry = tkr.scrolledtext.ScrolledText(coloscopicDataFrame2,height=5,width=60, font=("Arial",15), highlightbackground="#272727", highlightcolor="#272727")
    hallazgosColposcopicosLabel.grid(row=0,column=0,padx=10,pady=5,columnspan=3,sticky="N")
    hallazgosColposcopicosEntry.grid(row=1,column=0,padx=10,pady=5,columnspan=3)
    
    comtPlanTerapeuticoLabel = ttk.Label(coloscopicDataFrame2,text="COMENTARIOS Y PLAN TERAPEUTICO:")
    comtPlanTerapeuticoEntry = tkr.scrolledtext.ScrolledText(coloscopicDataFrame2,height=5,width=60, font=("Arial",15), highlightbackground="#272727", highlightcolor="#272727")
    comtPlanTerapeuticoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="N",columnspan=3)
    comtPlanTerapeuticoEntry.grid(row=3,column=0,padx=5,pady=10,columnspan=3)


    diagnosticoColposcopicoLabel = ttk.Label(coloscopicDataFrame2,text="DIAGNOSTICO COLPOSCOPICO:")
    diagnosticoColposcopicoEntry = ttk.Combobox(coloscopicDataFrame2)
    diagnosticoColposcopicoEntry['value'] = ("Selecciona","SIN ALTERNACIONES","ALTERNACIONES INFLAMATORIAS","LESIÓN Grado 1 (Menor)","LESIÓN Grado 2 (Mayor)","LESIÓN SUGESTIVA DE INVASIÓN")
    diagnosticoColposcopicoEntry.current(0)
    diagnosticoColposcopicoLabel.grid(row=4,column=0,padx=10,pady=5)
    diagnosticoColposcopicoEntry.grid(row=5,column=0,padx=10,pady=5)
    

    doctor1NameLabel = ttk.Label(coloscopicDataFrame2,text="DR (A):")
    doctor1NameEntry = ttk.Combobox(coloscopicDataFrame2)
    doctor1NameEntry['values'] = ("Selecciona","Alan Ariel Ortiz Ceceña")
    doctor1NameEntry.current(1)
    doctor1NameLabel.grid(row=4,column=1,padx=10,pady=5)
    doctor1NameEntry.grid(row=5,column=1,padx=10,pady=5)
    
   
    
    cedProfLabel = ttk.Label(coloscopicDataFrame2,text="CED. PROF:")
    cedProfEntry = ttk.Combobox(coloscopicDataFrame2)
    cedProfEntry['values'] = ("Selecciona", "12124020")
    cedProfEntry.current(1)
    cedProfLabel.grid(row=4,column=2,padx=10,pady=5)
    cedProfEntry.grid(row=5,column=2,padx=10,pady=5)


    ImagesStrPaths = [tkr.StringVar() for _ in range(4)]

    def image_path(i):
        nonlocal ImagesStrPaths
        file_path = filedialog.askopenfilename(title=f"Seleccionar imagen {i + 1 }")
        nombredelavariable = file_path
        ImagesStrPaths[i].set(file_path)
        updateScreen(i)
    
    def updateScreen(i):
        if(i == 0):
            if(ImagesStrPaths[i].get() != ""):
                image1Label.config(text="Imagen 1 (✓)")
            else:
                image1Label.config(text="Imagen 1 (𐄂)")
        elif(i == 1):
            if(ImagesStrPaths[i].get() != ""):
                image2Label.config(text="Imagen 2 (✓)")
            else:
                image2Label.config(text="Imagen 2 (𐄂)")
        elif(i == 2):
            if(ImagesStrPaths[i].get() != ""):
                imagen3Label.config(text="Imagen 3 (✓)")
            else:
                imagen3Label.config(text="Imagen 3 (𐄂)")
        else:
            if(ImagesStrPaths[i].get() != ""):
                imagen4Label.config(text="Imagen 4 (✓)")
            else:
                imagen4Label.config(text="Imagen 4 (𐄂)")

    image1Label = ttk.Label(coloscopicDataFrame2,text="IMAGEN 1:")
    image1Entry = ttk.Button(coloscopicDataFrame2,text="Seleccionar Imagen 1",command=lambda : image_path(0))
    image1Label.grid(padx=10,pady=5,row=6,column=0) #4 y 1 . 5 y 1
    image1Entry.grid(row=7,column=0,padx=10,pady=5)
    
    
    image2Label = ttk.Label(coloscopicDataFrame2,text="IMAGEN 2:")
    image2Entry = ttk.Button(coloscopicDataFrame2,text="Seleccionar Imagen 2",command=lambda : image_path(1))
    image2Label.grid(padx=10,pady=5,row=6,column=1)#4 y 2 . 5 y2
    image2Entry.grid(row=7,column=1,padx=10,pady=5)
  
    imagen3Label = ttk.Label(coloscopicDataFrame2,text="IMAGEN 3")
    imagen3Entry = ttk.Button(coloscopicDataFrame2,text="Seleccionar Imagen 3",command=lambda : image_path(2))
    imagen3Label.grid(row=6,column=2,padx=10,pady=10)
    imagen3Entry.grid(row=7,column=2,padx=10,pady=10)
    
    imagen4Entry = ttk.Button(colposcopicFrame,text="Selecciona Imagen 4",command=lambda : image_path(3))
    imagen4Entry.grid(row=10,column=0,padx=10,pady=10)
    imagen4Label = ttk.Label(colposcopicFrame,text="Imagen 4")
    imagen4Label.grid(row=9,column=0,padx=10,pady=10)
        
    
    ############################## BUTONES ############################
    
    buttonFrame = ttk.Labelframe(frame, text="Frame EXAMPLE")
    #buttonFrame.grid(row=0,column=2,rowspan=3,sticky="news",padx=20,pady=20)
    
    saveButton = ttk.Button(frame,text="Guardad",command=submission)
    saveButton.grid(row=0,column=3,padx=10,pady=10,sticky="news")
    
    menuReturnButton = ttk.Button(frame,text="Menu Principal")
    menuReturnButton.grid(row=1,column=3,padx=10,pady=10,sticky="news")
    
    cleanButton = ttk.Button(frame,text="Limpiar Campos")
    
    
    l = tkr.Button(buttonFrame,height=10,text="vemos")
    window.mainloop();



#filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif")]
