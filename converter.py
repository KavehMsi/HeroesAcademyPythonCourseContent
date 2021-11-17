
import os
import pathlib

NOTEBOOK = '.ipynb'

ignore_list = ['.git', '.ipynb_checkpoints']
path = pathlib.Path.cwd()
print(path)


for directory in path.iterdir():
    if directory.is_dir() and not directory.name in ignore_list:
        os.system("cd " + str(directory))
        for file in directory.iterdir():
            if file.is_file():
                if file.suffix == NOTEBOOK:
                    print("Converting", file, "To PDF: ")
                    command = 'jupyter-nbconvert --to PDFviaHTML "' + \
                        str(file) + '"'
                    os.system(command)
                if file.suffix == ".ppt" or file.suffix == ".pptx":
                    print("Converting", file, "To PDF: ")
                    os.system('ppt2pdf file "' + str(file) + '"')
print("All Good")
