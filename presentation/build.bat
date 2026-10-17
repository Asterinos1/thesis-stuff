@echo off
cd /d "%~dp0"
pdflatex -interaction=nonstopmode presentation.tex
pdflatex -interaction=nonstopmode presentation.tex
echo Compilation finished.
pause
