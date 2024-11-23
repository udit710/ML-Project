from setuptools import setup, find_packages

def get_requirements():
    '''
    Get the requirements from the requirements.txt file
    '''
    with open('requirements.txt') as f:
        req = [line.replace('\n','') for line in f.read().splitlines() if line]
        req.remove('-e .')
    return req

setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='Udit'
)