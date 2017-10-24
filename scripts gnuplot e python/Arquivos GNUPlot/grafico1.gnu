#reset

# eps => extensão de saída; font "NomeDaFonte, Tamanho"
set terminal postscript eps color font "Helvetica, 75"

# codificação dos caracteres
set encoding utf8

# output [arquivo_de_saida.extensão]
set output "saida/grafico1.eps"

# tamanho do arquivo
set size 4.0,4.0	# tamanho do grafico

# rmargin [tamanho] => margem da direita; lmargin [tamanho] => margem da esquerda
#set rmargin 2.5
#set lmargin 7

# posicionamento da legenda (keys) do gráfico
#set key left bottom 
#set key right bottom
#set key left top
set key right top

# mostra 'grade' no gráfico
set grid	

# título do gráfico
set title "Número de decisões em intervalos de 10s"

# rótulo do eixo X
set xlabel "Velocidades"

# rótulo do eixo y
set ylabel "Decisões"

# intervalo do eixo Y
set yrange [0:30]

# intervalo entre pontos do eixo y "0, 2, 4, 6, ..., 30	
set ytic 2			

# estilo de gráfico
set style data histogram  

# estilo da barra; errobars => intervalo de confianca; gap [numero] => espacamento entre os histogramas
set style histogram errorbars gap 5 

# estilo das bordas
set style fill solid border -1

# largura da barra
set boxwidth 1

# legendas dos histogramas
set xtics  ("Pedestre(1m/s)" 0, "Ciclista(3m/s)" 1, "Motorista(12m/s)" 2)

# cria os histogramas usando o arquivo: grafico1.txt

# A linha abaixo usa a linha 2 como valor do eixo y; a linha 5
# como limite inferior do intervalo de confianca e a linha 6 como intervalo 
# superior do intervalo de confianca
# O mesmo para as linhas seguintes
# lc => cor, preenchimento
# lt => line type
# t => title
# QUANDO MAIS DE UMA COMBINACAO USAR ',' E '\' PARA QUEBRA DE LINHA
plot 'grafico1.txt' using 2:5:6 t "BSR" lt 1  lc rgb "#000000", \
     'grafico1.txt' u 3:7:8 t "MSR" lt 1  lc rgb "#828282", \
     'grafico1.txt' u 4:9:10 t "ASR"  lt 1 lc rgb "#B5B5B5", \


