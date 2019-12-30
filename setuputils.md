# Fichier d'installation avec setuputils

##  A revoir
??? A voir\
dans les fichiers python:

    from euronext import euronext
    >>> euronext()

## Créer une distribution source 

    >>> python setup.py sdist
    >>> ls dist

## installation

    >>> mkdir ~/packages
    >>> cp dist/euronext.tar.gz ~/packages
    >>> pip install --no-index --find-links=~packages euronext

## uninstall

    >>> pip uninntall euronext
