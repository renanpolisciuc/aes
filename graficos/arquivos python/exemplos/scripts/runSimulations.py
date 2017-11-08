import os
import sys

# Numero de simulacoes
nSimulacoes = 35

# Lista de numero de redes
numRedes = ['2', '10', '20']

# Lista de tempos de decisao 
valoresTempoDecisao = ['10', '15', '20']

# Lista de velocidades
velocidades = ['1', '3', '12']

# Tempo total de simulacao
tempoSimulacao = '200'

# Largura do cenario. A altura eh igual a largura.
# Area = Largura * Altura = (Largura)^2
larguraCenario = '10'


for num_rede in numRedes:
	for intervalo_decisao in valoresTempoDecisao:
		for valor_velocidade in velocidades:
			for i in range (nSimulacoes):
				command = './waf --run "scratch/cenario1 --r='+num_rede 
                                command += ' --a='+larguraCenario                        
                                command += ' --v='+valor_velocidade                      
                                command += ' --i_d='+intervalo_decisao                   
                                command += ' --t_s='+tempoSimulacao+'"'
				result = os.system (command)  
				if result == 32512:
					print "[ERRO] Arquivo nao encontrado."
					exit (32512);
					                 
				print "[S="+str(i)+"] "+str(result) 
