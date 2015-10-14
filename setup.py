try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='bottle-swagger',
      version='0.1.0',
      url='https://github.com/nshgraph/bottle-swagger',
      description='Extract swagger specs from your bottle project',
      author='Nathan Holmberg',
      license='MIT',
      py_modules=['bottle_swagger'],
      long_description=long_description,
      install_requires=['bottle>=0.12.8', 'PyYAML>=3.0'])
