# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib
# We need a go through our lab folder 
# We need to find all the files and
# We need to find the directors
# We need check through Python files
# We need to add format for nicer view

lab = pathlib.Path("/Users/trishanmezbah20/Downloads/python-101-main")
for filepath in lab.iterdir():
    if filepath.is_dir():
        for lab_folder in filepath.iterdir():
            if lab_folder.suffix == ".py":
                print(lab_folder.name)
        
    else:

        if filepath.suffix == ".py":
            print(filepath.name)