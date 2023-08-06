from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dcmrtstruct2nii',
    version='1.0.10',
    description='Convert DICOM RT-Struct to nii',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Thomas Phil',
    author_email='thomas@tphil.nl',
    packages=find_packages(),  #same as name
    install_requires=[
        'numpy==1.15.4',
        'pydicom==1.2.1',
        'scikit-image==0.14.1',
        'scipy==1.2.0',
        'SimpleITK==1.2.0',
        'cleo==0.7.2'
    ], #external packages as dependencies
    scripts=[
        'bin/dcmrtstruct2nii'
    ]
)
