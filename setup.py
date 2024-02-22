from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    this function will return list of required libraries
    """

    requirements=[]
    with open(file_path) as f:
        requirements= f.readlines()
        #while readlines it will read \n also hence we will replace it with ""
        requirements = [req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlProject",
    version="0.0.1",
    author="jay",
    author_email="jayhegshetye@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
