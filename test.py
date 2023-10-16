from openConfig import folioLoad
import os
import json
db_file = os.path.join(os.path.dirname(__file__), 'documents/DB.json')

with open(db_file,"r") as file:
    path = json.load(file);
    
for i in path:
    if(i.get('folio')):
        print(i.get('folio'))
print(len(path))
        
        
        
        