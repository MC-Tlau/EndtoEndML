from setuptools import find_packages, setup

def get_requirements(file_path: str):
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e ')]
    return requirements

setup(
    name='projecto',
    version='0.0.1',
    author='Mercy',
    author_email='mercy2049@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
