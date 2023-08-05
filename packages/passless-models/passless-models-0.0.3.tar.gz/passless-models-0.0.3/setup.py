from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='passless-models',
    version='0.0.3',
    description='Models for Passless infrastructure.',
    long_description=readme(),
    author='Jesse de Wit',
    author_email='witdejesse@hotmail.com',
    url='https://github.com/JssDWt/passless-models',
    license='GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=['simplejson==3.16.0' , 'python-dateutil==2.7.5'],
)