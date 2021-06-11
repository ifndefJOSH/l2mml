#!/bin/bash

pyinstaller L2M.py

# For some reason, pyinstaller misses this *one* file, which I had to find in the pip install directory
# for the latex2mathml backend
mkdir ./dist/L2M/latex2mathml
cp unimathsymbols.txt dist/L2M/latex2mathml/
