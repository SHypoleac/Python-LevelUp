import json

print("'LoadJs(PATH)' to Load and WriteJs(PATH,FILE) to Write : \n")
def LoadJs(path):
    with open(path, "r") as file:
        from_file_data = file.read()
        return json.loads(from_file_data)

def WriteJs(path,file):
    with open(path, "w") as file:
        file.write(path)
