# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""
import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='tw-stock-plugin',
    version='0.1.4',
    author='Jimmy Yeh',
    author_email='chienfeng0719@hotmail.com',
    description='Some util function when doing Taiwan stock web scraping and some common stock data parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chienfeng0719/tw-stock-plugin',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pandas==1.1.0',
        'numpy==1.19.1',
        'requests==2.24.0',
        'lxml==4.5.2',
        'schema==0.7.2'
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    python_requires='>=3.6',
)
