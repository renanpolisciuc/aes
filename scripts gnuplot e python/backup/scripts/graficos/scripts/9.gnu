reset
set terminal postscript eps color font "Helvetica, 75"	#estilo da fonte
set encoding utf8	# formato da codificação das fontes
set output "comparacao_10s.eps"	# arquivo de saida


set sample 25
set size 4.5,4.5	# tamanho do grafico

#set rmargin 2.5
#set lmargin 7

#definicao da posicao da legenda
#set key left bottom  #(Canto inferior esquerdo)
#set key right bottom  #(Canto inferior direito)
#set key left top     #(Canto superior esquerdo)



set grid	# cria a grade pontilhada no grafico

set title "Comparação entre número de decisões e transições em intervalos de 10s"
set xlabel "Velocidades"			# legenda eixo X
set ylabel "Decisões/Transições"	# legenda eixo Y

#set auto x
set yrange [0:30]	# intervalo do eixo Y
set ytic 2			# intervalo entre os pontos do eixo Y

set grid
set style data histograms
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 1
set key inside right top horizontal spacing 1 width -2
set xtics border in scale 0,0 nomirror rotate by 0  autojustify
set xtics  norangelimit font ",50"
set xlabel  offset character 0, -2, 0 font "" textcolor lt -1 norotate



plot '8.txt' u 2:xtic(1) t "Decisões-BSR" lt 1 lw 1.0 lc rgb "#000000", \
  '' u 3 t "Transições-BSR"  fs pattern 1 border -1 lt -1 lw 1.0 lc rgb "#000000", \
  '' u 4 t  "Decisões-MSR" lt -1 lw 1.0 lc rgb "#626262" ,\
  '' u 5 t "Transições-MSR"  fs pattern 4 border -1 lt -1 lw 1.0 lc rgb "#626262", \
  '' u 6 t  "Decisões-ASR" lt -1 lw 1.0 lc rgb "#B5B5B5" , \
  '' u 7 t "Transições-ASR" fs pattern 5 border -1 lt -1 lw 1.0 lc rgb "#B5B5B5" , \
############### Descricao ##################
# col:linha [xtic(1)] --> o eixo x recebe o nome dos valores da coluna 1
# xtic(1) --> fixa a coluna 1 como eixo X para a combinacao com todas as outras colunas
# lt --> tipo da linha
# lc --> cor da barra
# u --> argumento que define as colunas do arquivo dados 
# t --> titulo da barra que ja vai para legenda

# QUANDO MAIS DE UMA COMBIACAO USAR ',' E '\' PARA QUEBRA DE LINHA
