import zipfile
import os
import glob

# Put all variables as str in quotes
# extensions in example as --> "[.exe,.sh,.py]"

def create_zip(path_to_folder,extensions,output_path):
    extensions="**/*"+extensions
    files=glob.glob(os.path.join(path_to_folder,extensions),recursive=True)
    with zipfile.ZipFile(output_path,"w") as zippp:
        for file in files:
            zippp.write(file)