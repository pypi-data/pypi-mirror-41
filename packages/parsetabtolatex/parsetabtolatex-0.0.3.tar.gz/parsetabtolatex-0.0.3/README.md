*parsetabtolatex* parses an output file of [ply](https://www.dabeaz.com/ply/) and extracts the grammar into a .tex file using the grammar environment provided by the [syntax](http://texdoc.net/texmf-dist/doc/latex/mdwtools/syntax.pdf) LaTeX package.

|               Author |     License | Homepage                                                      |
|----------------------|-------------|---------------------------------------------------------------|
Maria Climent-Pommeret | MIT Licence | https://gitlab.climent-pommeret.red/Chopopope/parsetabtolatex |


Installation
------------

Please run the following command in a virtual environment using Python3.5

    pip install parsetabtolatex

Usage example
-------------

    In[1]: from parsetabtolatex import parsetabtolatex as pl
    
    In[2]: pl.ParseTabToLatatex("/tmp/partetab.py", "/tmp/grammar.tex").generate_latex()



