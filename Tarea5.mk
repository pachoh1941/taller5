GRAFICOSCircuitoRC = histR.png graf_RvLike.png histC.png graf_CvLike.png graf_modelo.png 
circuitoRC.py : CircuitoRC.txt
plots_canal_ionico.py : Canal_ionico.txt canal_ionico.c Resultados.txt
    cc canal_ionico.c ./a.out
circulo.png : plots_canal_ionico.py
    python plots_canal_ionico.py
GRAFICOSCircuitoRC : circuitoRC.py
    python circuitoRC.py
Resultados_hw5.pdf : Resultados_hw5.tex GRAFICOSCanalesIonicos GRAFICOSCircuitoRC
    pdflatex Resultados_hw5.tex