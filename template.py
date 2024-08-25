import os
from pathlib import Path
import logging

# Logging String
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project = 'Kidney-Tumor-Classification'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project}/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/config/__init__.py",
    f"src/{project}/config/configuration.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")