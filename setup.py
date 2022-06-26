from setuptools import setup, find_packages
from typing import List

'''
You can declare variables here and pass in setup
'''
requirement_file_name = "requirements.txt"

def get_requirements_list():
    """
    DESCRIPTION : This function is going to return list of requirement
    mentioned in requirements.txt file

    this returns a list which contains libraries for main

    """


    with open(requirement_file_name) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
name = "housing-predictor",
version = '0.0.2',
author = "Harshit Srivastava",
description = "This is the first ml project",
packages = ["housing"],
install_requires = get_requirements_list()
)

