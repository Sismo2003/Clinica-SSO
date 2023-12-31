from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from openConfig import loadpath
import tkinter as tkr
import sys,os
import json
import time
from openConfig import folioLoad
import io

def createDocument(
    fullNamestr,pregnanciesstr,clientAgeEntrystr,MedicToEntrystr,dateofExamsEntrystr,birthsEntrystr,abortionEntrystr,
    fumFinalResultstr,cSectionEntrystr,vaginaVulvaEntrystr,cervixEntrystr,patronVascularEntrystr,zonaDeTransformacionEntrystr,
    unionEscamocilindricaEntrystr,epitelioEscamosoEntryst,EpitelioCilindricoEntrystr,TestDeHinselmaEntryst,TestDeScillerEntryst,
    ColposcopiaQuestionEntrystr,hallazgosColposcopicosEntrystr,comtPlanTerapeuticoEntryst,doctor1NameEntryst,cedProfEntryst,
    diagnosticoColposcopico,ImagesStrPaths
    ):

    
    
    try:

        Template_Path = os.path.join(os.path.dirname(__file__), loadpath('DocxTemplatePath'))

        ColoscopiaTemplateDoc = DocxTemplate(Template_Path)
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
            "id" : folioLoad('id')
        }
        contexDB = {
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
            "id" : folioLoad('id')
        }
    except:
        tkr.messagebox.showwarning(title="Error (xFDoCreate01)",message="Error al crear el documento. (error xFDoCreate01)")
    try:
        rango = 1
        for i in ImagesStrPaths:   
            if(i != "") :
                variable= f"image{rango}"
                rango +=1
                pathImages = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), i) 
                print(pathImages) 
                contex[variable]=InlineImage(ColoscopiaTemplateDoc,pathImages, width=Mm(25), height=Mm(20))
        filename = ""
        fullNamestr = fullNamestr.title()
        for i in fullNamestr:
            if(i != " "):
                filename+=i;
    
        
    except:
        tkr.messagebox.showerror(title="Error (xFDoCreate02)", message="Error al crear el documento. (xFDoCreate02)")
     
    try:
        ColoscopiaTemplateDoc.render(contex)
        FinalDocxPath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), loadpath('DocxSaveDocument'))
        output = os.path.join(FinalDocxPath, f"{filename}ReporteColposcopico.docx")
        ColoscopiaTemplateDoc.save(output)
        DBpath =os.path.join(os.path.dirname(__file__), loadpath('DatabasePath'))
        with open(f"{DBpath}","r") as file:
            path = json.load(file);
        path.append(contexDB)
        with open(f"{DBpath}","w") as file:
            json.dump(path,file,indent=4)
        os.system(f"open {FinalDocxPath}/{filename}ReporteColposcopico.docx")
        return True  
    except:
        tkr.messagebox.showerror(title="Error (xFDoCreate03)", message="Error al crear el documento. (xFDoCreate03)")
        return False
    
    #####base de datos
