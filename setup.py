
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='genalgo',  
     version='0.1',
     scripts=['genalgo'] ,
     author="Alison Wong",
     author_email="a.wong@sydney.edu.au",
     description="A genetic algorithm",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="",
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 4 - Beta",
         "Programming Language :: Python :: 3",
     ],
    install_requires=[
        'numpy',
        'matplotlib',
        'bz2',
        'pickle',
        'sys',
        'os'
    ]
 )