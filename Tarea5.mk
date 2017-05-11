GRAFICOSCanalesIonicos = graf_x.png graf_y.png circulo.png
GRAFICOSCircuitoRC = graf_RvLike.png graf_CvLike.png graf_modelo.png
circuitoRC.py : CircuitoRC.txt
plots_canal_ionico.py : Canal_ionico.txt canal_ionico.c
    cc canal_ionico.c ./a.out
GRAFICOSCanalesIonicos : plots_canal_ionico.py
    python plots_canal_ionico.py
GRAFICOSCircuitoRC : circuitoRC.py
    python circuitoRC.py
Resultados_hw5.pdf : Resultados_hw5.tex GRAFICOSCanalesIonicos GRAFICOSCircuitoRC
	pdflatex Resultados_hw5.tex