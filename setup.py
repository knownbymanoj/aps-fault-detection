# this is used to convert your code into library format
from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."
def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Manoj Kumar Nagabandi",
    author_email="manojnagabandi@gmail.com",
    packages= find_packages(), # to sreach for __init.py__ since we want to ue our code as a library 
    install_requires=get_requirements(),
)