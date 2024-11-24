#!/bin/bash

source /app/venv/bin/activate

python generate_pdf.py

pdflatex -output-directory=./output ./document.tex
