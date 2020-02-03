all: macros.tex proposal/doc/doc.pdf

macros.tex: proposal/doc/doc.pdf

proposal/doc/doc.pdf: proposal/doc/doc.tex
	./latexrun proposal/doc/doc.tex -o proposal/doc/doc.pdf
