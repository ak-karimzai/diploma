file-name := main-page
practic := practice

all: pdf

pdf:
	lualatex -interaction=nonstopmode ${file-name}.tex

practic:
	lualatex -interaction=nonstopmode ${practic}.tex

bib:
	biber --nodieonerror ${file-name}

practice-bib:
	biber --nodieonerror ${practic}

with-bib:
	${MAKE} pdf -i
	${MAKE} bib
	${MAKE} pdf -i
	${MAKE} pdf -i
	${MAKE} clean

practic-with-bib:
	${MAKE} practic -i
	${MAKE} practice-bib
	${MAKE} practic -i
	${MAKE} practic -i
	${MAKE} clean

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.blg *.bbl *.bcf *.run.xml 