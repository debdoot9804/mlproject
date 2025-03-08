from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List:
    """Returns list of requirements"""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]#to remove new line added in requirements.txt when we type new package



setup(
    name="ML_Project",
    version="0.0.1",
    author="Debdoot",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)

