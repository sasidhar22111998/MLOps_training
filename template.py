import os
from pathlib import Path

print("hello")

print(Path("a\\b\\c.txt"))

list_of_files=[
    ".github\\workflows\\.gitkeep",
    "src\\__init__.py",
    "src\\components\\__init__.py",
    "src\\components\\data_ingestion.py",
    "src\\components\\data_transformation.py",
    "src\\components\\model_trainer.py",
    "src\\components\\model_evaluation.py",
    "src\\pipeline\\__init__.py",
    "src\\pipeline\\training_pipeline.py",
    "src\\pipeline\\prediction_pipeline.py",
    "src\\utils\\__init__.py",
    "src\\utils\\utils.py",
    "src\\logger\\logging.py",
    "src\\exception\\exceptions.py",
    "tests\\unit\\__init__.py",
    "tests\\integration\\__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments\\experiments.ipynb"

]

for path in list_of_files:
    # Extract directory and filename
    dir_path, file_name = os.path.split(path)
        
    # Create directories if they don't exist
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Directory created: {dir_path}")
        
    # Create the file if a filename is specified
    if file_name:
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as f:
            pass  # Create an empty file
        print(f"File created: {file_path}")