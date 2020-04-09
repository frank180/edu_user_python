#!/usr/bin/env python

from setuptools import setup, Extension

VERSION = '1.1'

setup(
    name= 'npu_tool',
    version= VERSION,
    url='https://github.com/frank180/edu_user_python',
    author='yan',
    author_email="yan-wyb@foxmail.com",
    maintainer='frank',
    maintainer_email= 'frank@khadas.com',
    description='A amlogic npu usertool library in khadas VIMs board',
    classifiers=[
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: GPLv2 License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    platforms=['Linux'],
    license='GPLv2',
    py_modules = ['npu_tool'],
)

