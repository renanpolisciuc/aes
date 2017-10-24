#reset

# eps => extensão de saída; font "NomeDaFonte, Tamanho"
set terminal postscript eps color font "Helvetica, 75"  #estilo da fonte

# codificação dos caracteres
set encoding utf8

# output [arquivo_de_saida.extensão]
set output "saida/grafico4.eps"

# numero de pontos do eixo X (http://www.gnuplotting.org/tag/samples/)
set sample 25

# tamanho do gráfico
set size 7.0,7.0

# http://gnuplot.sourceforge.net/docs_4.2/node157.html
set autoscale

# grades do gráfico
set grid

# http://gnuplot.sourceforge.net/docs_4.2/node173.html
set datafile missing '-'

# tipo de gráfico
set style data linespoints

# intervalo do eixo y
set yrange [0:35]

#intervalo entre os pontos do eixo y
set ytic 1      

# intervalo do eixo x
set xrange [0:30]


# relacionado ao estilo do gráfico também
set style function lines

# http://www.manpagez.com/info/gnuplot/gnuplot-4.4.0/gnuplot_272.php
set offsets 0.05, 0.05, 0, 0

# rótulo do eixo y
set ylabel "Número de decisões"

# rótulo do eixo x
set xlabel "Simulação"

# título do gráfico
set title "Número de decisões nos intervalos de 10 e 20 segundos para um ciclista"



# cada linha usa os dados de um arquivos
# lc => cor, preenchimento
# lt => line type
# t => title
# lw => line width
# pt => tipo de ponto
# QUANDO MAIS DE UMA COMBINACAO USAR ',' E '\' PARA QUEBRA DE LINHA
plot 'grafico4_1.txt' using 2:xtic(1) title 'BSR-10s' lt 5 lw 10.0 pt 4 ps 5 lc rgb "#FF0000" , \
     'grafico4_2.txt' u 2:xtic(1) title 'MSR-10s' lt 5 lw 10.0  pt 4 ps 5 lc rgb "#008000", \
     'grafico4_3.txt' u 2:xtic(1) title 'ASR-10s' lt 5 lw 10.0 pt 4 ps 5 lc rgb "#0000FF", \
     'grafico4_4.txt' using 2:xtic(1) title 'BSR-20s' lt 2 lw 10.0 pt 3 ps 5 lc rgb "#FF0000" , \
     'grafico4_5.txt' u 2:xtic(1) title 'MSR-20s' lt 2 lw 10.0  pt 3 ps 5 lc rgb "#008000", \
     'grafico4_6.txt' u 2:xtic(1) title 'ASR-20s' lt 2 lw 10.0 pt 3 ps 5 lc rgb "#0000FF"