file-name := main-page

all: pdf

pdf:
	lualatex -interaction=nonstopmode ${file-name}.tex

bib:
	biber --nodieonerror ${file-name}

with-bib:
	${MAKE} pdf
	${MAKE} bib
	${MAKE} pdf
	${MAKE} pdf
	${MAKE} clean

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.blg *.bbl *.bcf *.run.xml 