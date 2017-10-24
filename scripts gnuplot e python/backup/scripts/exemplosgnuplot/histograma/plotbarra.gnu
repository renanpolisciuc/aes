reset
set terminal postscript eps color font "Helvetica, 75"	#estilo da fonte
#set terminal postscript png color font "Helvetica, 75"	#estilo da fonte
set encoding iso_8859_1	# formato da codificação das fontes
#set output "barra.eps"	# arquivo de saida
set output "barra.png"

set size 4.0,4.0	# tamanho do grafico

#set rmargin 2.5
#set lmargin 7

#definicao da posicao da legenda
#set key left bottom  #(Canto inferior esquerdo)
#set key right bottom  #(Canto inferior direito)
#set key left top     #(Canto superior esquerdo)
set key right top    #(Canto superior direito)

set grid	# cria a grade pontilhada no grafico

set title "Crescimento de ERB por operadora no Brasil"
set xlabel "Anos"			# legenda eixo X
set ylabel "Crescimento (milhares)"	# legenda eixo Y

#set auto x
set yrange [12000:15500]	# intervalo do eixo Y
set ytic 500			# intervalo entre os pontos do eixo Y

set style data histogram	# estilo do grafico em histograma-barra
set style histogram cluster gap 1	#distancia entre o grupo de barras
set style fill solid border -1	# estilo da linha de contorno da barra
set boxwidth 1			# largura da barra

plot 'dados.txt' using 2:xtic(1) t "VIVO" lt 1 lc rgb "#1C1C1C", \
		'' u 3 t "OI" lt 1 lc rgb "#4F4F4F", \
		'' u 4 t "TIM" lt 1 lc rgb "#828282", \
		'' u 5 t "Claro" lt 1 lc rgb "#B5B5B5"

############### Descricao ##################
# col:linha [xtic(1)] --> o eixo x recebe o nome dos valores da coluna 1
# xtic(1) --> fixa a coluna 1 como eixo X para a combinacao com todas as outras colunas
# lt --> tipo da linha
# lc --> cor da barra
# u --> argumento que define as colunas do arquivo dados 
# t --> titulo da barra que ja vai para legenda

# QUANDO MAIS DE UMA COMBIACAO USAR ',' E '\' PARA QUEBRA DE LINHA
