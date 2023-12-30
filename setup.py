from setuptools import setup 
  
# reading long description from file 
with open('DESCRIPTION.txt') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = [] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 1 - Beta', 
    'Intended Audience :: Developers', 
    'Topic :: Internet', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    'Programming Language :: Python :: 3.6', 
    'Programming Language :: Python :: 3.7', 
    'Programming Language :: Python :: 3.8', 
    'Programming Language :: Python :: 3.9', 
    'Programming Language :: Python :: 3.10', 
    'Programming Language :: Python :: 3.11', 
    'Programming Language :: Python :: 3.12', 

    ] 
  
# calling the setup function  
setup(name='netsalary', 
      version='1.0.0', 
      description='A simple net salary calculator', 
      long_description=long_description, 
      url='https://github.com/mgemoraw/netsalary', 
      author='Mengistu Getie', 
      author_email='meng.get4@gmail.com', 
      license='MIT', 
      packages=[], 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='salary'
      ) 