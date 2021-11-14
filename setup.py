from setuptools import setup, find_packages

setup(
    name             = 'InSearch',
    version          = '0.1',
    description      = 'Python-based inverted index structure library with full-text search support',
    author           = '2ternal, Fortune00, MoonDD99, shellboy',
    author_email     = 'ddft97@gmail.com, sinyoungbok99@gmail.com, mjh991016@naver.com, qkrdmstlr3@naver.com',
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