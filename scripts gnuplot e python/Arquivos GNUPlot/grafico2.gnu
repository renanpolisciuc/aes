#reset
# eps => extensão de saída; font "NomeDaFonte, Tamanho"
set terminal postscript eps color font "Helvetica, 75"

# codificação dos caracteres
set encoding utf8

# output [arquivo_de_saida.extensão]
set output "saida/grafico2.eps"

# numero de pontos do eixo X (http://www.gnuplotting.org/tag/samples/)
set sample 25

# tamanho do gráfico
set size 4.5,4.5

# rmargin [tamanho] => margem da direita; lmargin [tamanho] => margem da esquerda
#set rmargin 2.5
#set lmargin 7


# cria a grade pontilhada no grafico
set grid	

# título do gráfico
set title "Comparação entre número de decisões e transições em intervalos de 10s"

# rótulo do eixo X
set xlabel "Velocidades"

# rótulo do eixo Y
set ylabel "Decisões/Transições"

# intervalo do eixo Y
set yrange [0:30]

# intervalo entre os pontos do eixo Y
set ytic 2		

# estilo do gráfico
set style data histograms

# estilo do gráfico; gap [numero] => espacamento entre os histogramas
set style histogram cluster gap 1

# tipo de borda
set style fill solid border -1

# largura das barras
set boxwidth 1

# posicionamento da legenda
set key inside left top horizontal spacing 1 width -2

# posicionamento dos pontos do eixo X (legenda)
set xtics border in scale 0,0 nomirror rotate by 0  autojustify
set xtics  norangelimit font ",50"
set xlabel  offset character 0, -2, 0 font "" textcolor lt -1 norotate


# usa o arquivo de dados '8.txt'
# usa a segunda coluna do arquivo como dados de y para "Decisões-BSR" e a coluna 1 como valores de X
# usa a terceira coluna com dados de y para"Transições-BSR"
# ...
# lc => cor, preenchimento
# fs pattern [numero] => tipo de preenchimento das barras
# lw => line width
# lt => line type
# QUANDO MAIS DE UMA COMBINACAO USAR ',' E '\' PARA QUEBRA DE LINHA
plot 'grafico2.txt' u 2:xtic(1) t "Decisões-BSR" lt 1 lw 1.0 lc rgb "#000000", \
  '' u 3 t "Transições-BSR"  fs pattern 1 border -1 lt -1 lw 1.0 lc rgb "#000000", \
  '' u 4 t  "Decisões-MSR" lt -1 lw 1.0 lc rgb "#626262" ,\
  '' u 5 t "Transições-MSR"  fs pattern 4 border -1 lt -1 lw 1.0 lc rgb "#626262", \
  '' u 6 t  "Decisões-ASR" lt -1 lw 1.0 lc rgb "#B5B5B5" , \
  '' u 7 t "Transições-ASR" fs pattern 5 border -1 lt -1 lw 1.0 lc rgb "#B5B5B5" , \



