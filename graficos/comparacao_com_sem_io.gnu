#reset

# eps => extensão de saída; font "NomeDaFonte, Tamanho"
set terminal pdf size 12,8 color font "Helvetica, 11"

# codificação dos caracteres
set encoding utf8

# output [arquivo_de_saida.extensão]
set output "pdf/comparacao.pdf"

# tamanho do arquivo
set size 1,1	# tamanho do grafico

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
set title "Tempo execução - GPU - Comparação IO"

# rótulo do eixo X
set xlabel "Tamanhos dos arquivos"

# rótulo do eixo y
set ylabel "Tempo gasto (s)"

# intervalo do eixo Y
#set yrange [0:30]

# intervalo entre pontos do eixo y "0, 2, 4, 6, ..., 30
#set ytic 2

# estilo de gráfico
set style data histogram

# estilo da barra; errobars => intervalo de confianca; gap [numero] => espacamento entre os histogramas
set style histogram errorbars gap 5 lw 2

# estilo das bordas
set style fill solid border -1

set style line 1 lt 5 lw 1 pt 3 ps 0.5

# largura da barra
set boxwidth 1

# legendas dos histogramas
#set xtics  ("412KB" 0, "45MB" 1, "72MB" 2, "214MB" 3, "648MB" 4, "917MB" 5)

# cria os histogramas usando o arquivo: grafico1.txt

# A linha abaixo usa a linha 2 como valor do eixo y; a linha 5
# como limite inferior do intervalo de confianca e a linha 6 como intervalo
# superior do intervalo de confianca
# O mesmo para as linhas seguintes
# lc => cor, preenchimento
# lt => line type
# t => title
# QUANDO MAIS DE UMA COMBINACAO USAR ',' E '\' PARA QUEBRA DE LINHA
plot 'comparacao.txt' using  2:3:4:xtic(1) t "I/O" lt 2 lw 1 lc rgb "#009900", \
     'comparacao.txt' u 5:6:7:xtic(1) t "Processamento" lt 2 lw 1 lc rgb "#ffff00", \
     'comparacao.txt' u 8:9:10:xtic(1) t "Total" lt 2 lw 1 lc rgb "#993333", \
     #'Vazãos.txt' u 8:9:10:xtic(1) t "GPU - G" lt 2 lw 1 lc rgb "#33ccff", \
