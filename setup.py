from setuptools import setup, find_packages
from os import path

this = path.abspath(path.dirname(__file__))
with open(path.join(this, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name             = 'InSearch',
    version          = '0.1.3',
    description      = 'Python-based inverted index structure library with full-text search support',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author           = '2ternal, Fortune00, MoonDD99, shellboy',
    author_email     = 'ddft97@gmail.com',
    url              = 'https://github.com/CNUCSE-Team2/InSearch',
    install_requires = [ 'eunjeon >= 0.4.0'],
    packages         = find_packages(exclude = []),
    keywords         = ['BM25', 'inverted-index', 'full-text search'],
    python_requires  = '>=3',
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)