from dataclasses import dataclass

### Use save_merged_files(save_path, *path_of_files)
### to save merge files with the same titles into save_path directory

@dataclass()
class CSV_reader:
    """
    1 - Return header
    0 - Return all file
    -1 - Return body without header
    """
    path: str

    def __post_init__(self):
        with open(self.path, "r") as file:
            self.doc = file.read()

    def show(self, lines):
        match lines:
            case 0:
                doc = self.doc
            case 1:
                doc = self.doc.splitlines()[0]
            case -1:
                doc = "\n".join(self.doc.splitlines()[1:])
        return doc


def load_the_files(*paths_to_files):
    """
    Input --> PATH,*PATH\n
    Output --> list[n] of CSV_reader_objects
    """
    files = []
    for path in paths_to_files:
        obj = CSV_reader(path)
        files.append(obj)
    return files


def headers_checker(files):
    headers = []
    for file in files:
        headers.append(file.show(1))
    if all(header == headers[0] for header in headers):
        print("All headers are the same")
        return True
    else:
        info = "Headers arent identical :\n"
        info += "\n".join([f"{index} : {header}" for index,
                          header in enumerate(headers)])
        print(info)
        return False

def save_merged_files(save_path, *path_of_files):
    files = load_the_files(*path_of_files)
    if headers_checker(files):
        output = files[0].show(1)
        for file in files:
            output += (file.show(-1))
            output += "\n"
        with open(save_path, "w") as save_file:
            save_file.write(output)
