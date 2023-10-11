import os
from docx2pdf import convert

ruta_archivo = '/pacientes/AkeReporteColposcopico.docx'

convert(f"{ruta_archivo}")
ruta_archivo =  '/pacientes/AkeReporteColposcopico.pdf'
if os.path.exists(ruta_archivo):
    os.system(f"open {ruta_archivo}")

else:
    print(f"El archivo {ruta_archivo} no existe.")
