import os
import json
import shutil
from pprint import pprint

# Your old music location. This is a list just because uses the same function as SOURCE_LOCATIONS to retrive files
OLD_LOCATION=["/Volumes/SKODA/Albums"]
NEW_LOCATION="/Volumes/OCTAVIA" # Your new music location
# Your source music locations. Can be more than one, if you have music in more than one location.
SOURCE_LOCATIONS=["/Volumes/Multimedia/Music/Albums","/Volumes/Multimedia/Music/luis_avelar","/Volumes/Multimedia/Music/singles"]
MIMES=[".mp3",".wma"]
SCRIPT_PATH = os.path.dirname(__file__)
OLD_JSON = os.path.join(SCRIPT_PATH,"old_files.json")
SOURCE_JSON = os.path.join(SCRIPT_PATH,"source_files.json")

def get_files(folders:list,json_file:str):
    source_files={}
    if not os.path.exists(json_file):
        for source in folders:
            if not os.path.exists(source):
                print("The folder",source,"does not exists!")
                continue
            for root,dirnames,filenames in os.walk(source):
                for file in filenames:
                    _,ext = os.path.splitext(file)
                    if ext.lower() in MIMES:
                        file_path = os.path.join(root,file)
                        source_files[file_path.replace(source + os.path.sep,"")] = os.path.join(root,file)

        with open(json_file,"w") as f:
            json.dump(source_files,f)
    else:
        with open(json_file,"r") as f:
            source_files = json.load(f)
         
    return source_files

source_files = get_files(SOURCE_LOCATIONS,SOURCE_JSON)
old_files = get_files(OLD_LOCATION,OLD_JSON)
print("Do you start the copy now? Files already in the destination will not be copied.")
resp = input("Write \"no\" to stop or nothing to start: ")
if resp.lower() == "no":
    exit()
else:
    for key,value in old_files.items():
        file = source_files.get(key,None)
        if file:
            source_path = file.replace(key,"")
            dest_path = file.replace(source_path,"")
            dest_dir = os.path.join(NEW_LOCATION, os.path.dirname(dest_path))
            dest_filename = os.path.join(NEW_LOCATION, dest_path)
            print(file,",",dest_filename,",",dest_dir)
            if not os.path.exists(dest_filename):
                os.makedirs(dest_dir,exist_ok=True)
                shutil.copyfile(file,dest_filename)
        
        
        
