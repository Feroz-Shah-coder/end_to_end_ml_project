## Generateing and responsibe the project as pakage (Setup.py)
from setuptools import find_packages, setup
from typing import List

HYPON_E_DOT = "-e ."

def git_requirements(file_path:str)->list[str]:
    ## This fun return the requrments list
    requirements = [],
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace('\n',"") for req in requirements ]

    if HYPON_E_DOT in requirements:
        requirements.remove(HYPON_E_DOT)
    
    return requirements 

     


setup(
    name='ml_project',
    version='0.0.1',
    author='Feroz',
    author_email='ferozalimze@gmail.com',
    packages=find_packages(),
    install_requires=git_requirements('requirements.txt')
)