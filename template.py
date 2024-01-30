import os
from pathlib import Path

package_name = "Credit_Card_Default_Prediction"

list_of_files = [
    f".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_integration.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/pipelines/__init__.py", 
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipelines.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    "notebooks/research.ipynb",
    "notebooks/EDA_Data_Preprocessing.ipynb",
    "notebooks/Model_training.ipynb",
    "notebooks/data/.gitkeep",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    """ How exist_ok works : if 'directory' already exists,
    os.makedirs() will not raise an error, and it will do nothing.
    If 'my_directory' dosen't exist, it will create the directory. """
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file laready exist")
