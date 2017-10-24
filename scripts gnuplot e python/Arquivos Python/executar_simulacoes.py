import os
import sys


numeroSimulacoes = 35
comandoNS3 = "./waf --run scratch/"
arquivoExecutar = "cenario"
comando = comandoNS3+arquivoExecutar

for i in range (0, numeroSimulacoes):
	print "[LOG] Executando a iteracao "+str(i)
	print "[SYS] Comando: "+comando
	#os.system (comando)
	
