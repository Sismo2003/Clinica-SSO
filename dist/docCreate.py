from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from openConfig import loadpath
import tkinter as tkr
import os
from docx2pdf import convert
import json


def createDocument(
    fullNamestr,pregnanciesstr,clientAgeEntrystr,MedicToEntrystr,dateofExamsEntrystr,birthsEntrystr,abortionEntrystr,
    fumFinalResultstr,cSectionEntrystr,vaginaVulvaEntrystr,cervixEntrystr,patronVascularEntrystr,zonaDeTransformacionEntrystr,
    unionEscamocilindricaEntrystr,epitelioEscamosoEntryst,EpitelioCilindricoEntrystr,TestDeHinselmaEntryst,TestDeScillerEntryst,
    ColposcopiaQuestionEntrystr,hallazgosColposcopicosEntrystr,comtPlanTerapeuticoEntryst,doctor1NameEntryst,cedProfEntryst,
    diagnosticoColposcopico,ImagesStrPaths
    ):

    
    
    try:
        ColoscopiaTemplateDoc = DocxTemplate(f"{loadpath('DocxTemplatePath')}")
        contex = {
            "name" : fullNamestr,
            "preg" : pregnanciesstr,
            "clientAge" : clientAgeEntrystr,
            "medicTo" : MedicToEntrystr,
            "dateOfExams" : dateofExamsEntrystr,
            "births" : birthsEntrystr,
            "abortion" : abortionEntrystr,
            "fum" : fumFinalResultstr,
            "csec" : cSectionEntrystr,
            "vaginaVulvaEntry" : vaginaVulvaEntrystr,
            "cervix":cervixEntrystr,
            "patronVascular" : patronVascularEntrystr,
            "zonaDeTransformacion" : zonaDeTransformacionEntrystr,
            "unionEscamocilindrica":unionEscamocilindricaEntrystr,
            "epitelioEscamoso":epitelioEscamosoEntryst,
            "epitelioCilindrico":EpitelioCilindricoEntrystr,
            "testDeHinselman" : TestDeHinselmaEntryst,
            "testDeSchiller" : TestDeScillerEntryst,
            "colposcopia" : ColposcopiaQuestionEntrystr,
            "hallazgosColposcopicos": hallazgosColposcopicosEntrystr,
            "diagnosticoColposcopico" :diagnosticoColposcopico,
            "comtPlanTerapeutico" : comtPlanTerapeuticoEntryst,
            "doctorName" : doctor1NameEntryst ,
            "cedProf" : cedProfEntryst,
        }
    except:
        tkr.messagebox.showwarning(title="Error (xFDoCreate01)",message="Error al crear el documento. (error xFDoCreate01)")
    try:
        rango = 1
        for i in ImagesStrPaths:   
            if(i != "") :
                variable= f"image{rango}"
                rango +=1
                contex[variable]=InlineImage(ColoscopiaTemplateDoc,i, width=Mm(25), height=Mm(20))
        filename = ""
        fullNamestr = fullNamestr.title()
        for i in fullNamestr:
            if(i != " "):
                filename+=i;
    
        
    except:
        tkr.messagebox.showerror(title="Error (xFDoCreate02)", message="Error al crear el documento. (xFDoCreate02)")
     
    try:
        ColoscopiaTemplateDoc.render(contex)
        ColoscopiaTemplateDoc.save(f"{loadpath('DocxSaveDocument')}/{filename}ReporteColposcopico.docx")
        #convert(f"open {loadpath('DocxSaveDocument')}/{filename}ReporteColposcopico.docx")
        #os.remove(f"{loadpath('DocxSaveDocument')}/{filename}ReporteColposcopico.docx")
        #os.chmod(f"{loadpath('DocxSaveDocument')}", 0o666)
        #os.system(f"open {loadpath('DocxSaveDocument')}/{filename}ReporteColposcopico.pdf")
        with open(f"{loadpath('DatabasePath')}","r") as file:
            path = json.load(file);
        path.append(contex)
        with open(f"{loadpath('DatabasePath')}","w") as file:
            json.dump(path,file,indent=4)
        print(path)
        return True
        
        
    except:
        tkr.messagebox.showerror(title="Error (xFDoCreate03)", message="Error al crear el documento. (xFDoCreate03)")
        return False
    
    #####base de datos
