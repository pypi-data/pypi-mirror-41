import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name="pygame_plot",
    version="0.1",
    url="https://github.com/LSaffin/pygame_plot",
    license='MIT',

    author="Leo Saffin",
    author_email="string_buster@hotmail.com",

    description="Quick visualization of data using pygame with a matplotlib style",
    long_description=read("README.rst"),

    packages=find_packages(exclude=('tests',)),

    install_requires=['pygame', 'matplotlib', 'numpy'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
