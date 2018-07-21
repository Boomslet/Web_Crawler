from setuptools import setup, find_packages
from codecs import open
from os import path


setup(
    name='Web_Crawler',

    version='2.0.0',

    description='A light-weight web crawler',

    # The project's main homepage.
    url='https://github.com/Boomslet/Web_Crawler',

    # Author details
    author='Mark Boon',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='web webcrawl scrape',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['beautifulsoup4', 'lxml'],
)
