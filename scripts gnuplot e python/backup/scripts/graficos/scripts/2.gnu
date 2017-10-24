reset
set terminal postscript eps color font "Helvetica, 75"	#estilo da fonte
set encoding utf8	# formato da codificação das fontes
set output "numero_handovers_cenario_15_segundos.eps"	# arquivo de saida

set size 4.0,4.0	# tamanho do grafico

#set rmargin 2.5
#set lmargin 7

#definicao da posicao da legenda
#set key left bottom  #(Canto inferior esquerdo)
#set key right bottom  #(Canto inferior direito)
#set key left top     #(Canto superior esquerdo)
set key right top    #(Canto superior direito)

set grid	# cria a grade pontilhada no grafico

set title "Número de transições a partir de decisões em intervalos de 15s"
set xlabel "Velocidades"			# legenda eixo X
set ylabel "Transições"	# legenda eixo Y

#set auto x
set yrange [0:30]	# intervalo do eixo Y
set ytic 2			# intervalo entre os pontos do eixo Y

set style data histogram	# estilo do grafico em histograma-barra
set style histogram cluster gap 1	#distancia entre o grupo de barras
set style fill solid border -1	# estilo da linha de contorno da barra
set boxwidth 1			# largura da barra

plot '2.txt' using 2:xtic(1) t "BSR" lt 1 lc rgb "#000000" , \
	     '' u 3 t "MSR" lt 1 lc rgb "#828282", \
	     '' u 4 t "ASR"  lt 1 lc rgb "#B5B5B5" , \

############### Descricao ##################
# col:linha [xtic(1)] --> o eixo x recebe o nome dos valores da coluna 1
# xtic(1) --> fixa a coluna 1 como eixo X para a combinacao com todas as outras colunas
# lt --> tipo da linha
# lc --> cor da barra
# u --> argumento que define as colunas do arquivo dados 
# t --> titulo da barra que ja vai para legenda

# QUANDO MAIS DE UMA COMBIACAO USAR ',' E '\' PARA QUEBRA DE LINHA
