GRAFICOSCircuitoRC = histR.png graf_RvLike.png histC.png graf_CvLike.png graf_modelo.png 
Resultados_hw5.pdf : Resultados_hw5.tex circulo.png GRAFICOSCircuitoRC
	pdflatex Resultados_hw5.tex
GRAFICOSCircuitoRC : circuitoRC.py
	python circuitoRC.py
circulo.png : plots_canal_ionico.py
	python plots_canal_ionico.py
plots_canal_ionico.py : Canal_ionico.txt canal_ionico.c Resultados.txt
Resultados.txt : a.out
	./a.out
a.out : canal_ionico.c
	cc canal_ionico.c -lm
circuitoRC.py : CircuitoRC.txt
