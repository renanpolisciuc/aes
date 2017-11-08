reset	#limpa lixo da memoria do gnuplot
set terminal postscript
set output "./exemplo.eps"	# arquivo de saida
set title "Crescimento de ERB no Brasil"	#titulo do grafico

set style data lines	# utilização de grafico de linhas
set grid y		# Grafico com grades  

#set key left bottom  #(Canto inferior esquerdo)
#set key right bottom  #(Canto inferior direito)
#set key left top     #(Canto superior esquerdo)
set key right top    #(Canto superior direito)

set xlabel "Anos" # legenda do eixo X
set ylabel "Crescimentos" # legenda do eixo Y

set yrange [50000:60000] #intervalo do eixo Y
set xtic 2000	#intervalo entre cada ponto

set xrange [2011:2014]	#intervalo do eixo X
set xtic 1 #intervalo entre cada ponto

DADOS='./dados.txt' # carregamento do arquivo de dados


plot DADOS using 1:6 with linespoints title "ERB" linetype 1 lw 2 pt 7 linecolor rgb "#000000"


#################### lista de argumentos #######################
# u = using --> argumento que define as colunas do arquivo dados
# 1:2 --> colunas que estao relacionadas (x,y)
# w = with --> argumento que define tipo de linha, ponto, etc.
#lp = linespoints --> define o estilo da linha
# t = title --> define o titulo(legenda) da linha que vem entre " "
# lt = linetype --> define o tipo da linha
# pt = pointtype --> define o tipo do ponto
# lc = linecolor --> define a cor da linha
# QUANDO MAIS DE UMA COMBIACAO USAR ',' E '\' PARA QUEBRA DE LINHA
#'' --> define nova coluna combinada

