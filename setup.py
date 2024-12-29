from setuptools import setup, find_packages

setup(
    name='sino_nom_dictionary',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['../data/*', '../data/hvthivien_images/*']
    },
    install_requires=['numpy', 'Pillow', 'setuptools'],
    description='A dictionary for Sino-Nom Vietnamese characters',
    python_requires='>=3.6',
)