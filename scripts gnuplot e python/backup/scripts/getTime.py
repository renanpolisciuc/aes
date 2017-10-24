from __future__ import division
from math import sqrt
import os
import sys
import math

if len(sys.argv) < 9:
	print "python getTime.py [pasta de entrada] [prefixo de entrada] [extensao entrada] [pasta de saida] [prefixo de saida] [iteracoes] [Arquivo de log] [Ator] [Velocidade]"
	exit (-1)

folderIn = sys.argv[1]
prefixIn = sys.argv[2]
extensionIn = sys.argv[3]
folderOut = sys.argv[4]
prefixOut = sys.argv[5]
max_iterations = int (sys.argv[6])
counter = 0
decision = 0
decision_h = 0
tempo_decisao = 0
soma_decisoes = 0
max_handovers  = 0
min_handovers = -1
erros = 0
encontrou_erro = 0
handovers = []
lista_erros = []
decisoes_diferente_zero = 0
soma_tempo = 0
tempos = []
clean = os.system("rm -r "+folderOut+"*")
print "[LOG] Clean: ", clean
if clean <> 0:
	os.system("mkdir "+folderOut)	

while counter < max_iterations:
	fileIn = open (folderIn+prefixIn+str(counter)+extensionIn, "r")
	fileOut = open (folderOut+prefixOut+str(counter)+".out", "w")

	lines = fileIn.readlines ()
	for line in lines:
		findError = line.find("signal")
		if findError > -1:
			erros = erros + 1
			encontrou_erro = 1
                        lista_erros.append (counter)
		if line.find ("Decision") > -1 :
			find = line.find ("Miliseconds:")
			if find > -1:
                                decision_h = decision_h + 1
				tempo_decisao = tempo_decisao + int(line[find+len("Miliseconds:")+1::])
				tempos.append (line[find+len("Miliseconds:")+1::])
		if line.find ("DecisionModule:Run()") > -1 :
                        decision = decision+1
			

	if encontrou_erro <> 1:
		soma_decisoes = soma_decisoes + decision_h
	
	if decision_h > max_handovers:
		max_handovers = decision_h

	if min_handovers == -1 or min_handovers > decision_h:
		min_handovers = decision_h

        if encontrou_erro == 1:
                fileOut.write("[LOG] Arquivo["+folderIn+prefixIn+str(counter)+extensionIn+"] => ERRO ENCONTRADO!")
                print "[LOG] Arquivo["+folderIn+prefixIn+str(counter)+extensionIn+"] => ERRO ENCONTRADO!"
	elif decision_h == 0:
		fileOut.write("[LOG] Arquivo["+folderIn+prefixIn+str(counter)+extensionIn+"] => Handovers: "+str(decision_h)+"; Media de tempo das decisoes: "+str(0))
		print "[LOG] Arquivo["+folderIn+prefixIn+str(counter)+extensionIn+"] => Handovers: "+str(decision_h)+"; Media de tempo das decisoes: "+str(0)
	else:
		decisoes_diferente_zero = decisoes_diferente_zero + 1
		soma_tempo = soma_tempo + (tempo_decisao/decision_h)
		fileOut.write("[LOG] Arquivo["+folderIn+prefixIn+str(counter)+extensionIn+"] => Handovers: "+str(decision_h)+"; Media de tempo das decisoes: "+str(tempo_decisao/decision_h))
		print "[LOG] Arquivo["+folderIn+prefixIn+str(counter)+extensionIn+"] => Handovers: "+str(decision_h)+"; Media de tempo das decisoes: "+str(tempo_decisao/decision_h)
	fileOut.write ("[LOG] Tempos: " + str(tempos))
	handovers.append(decision_h)
	fileIn.close ()
	fileOut.close ()
	decision_h = 0
	encontrou_erro = 0
	tempo_decisao = 0
	counter = counter + 1
	tempos = []

arquivo_log = sys.argv[7]
ator = sys.argv[8]
velocidade = sys.argv[9]

max_iterations = max_iterations - erros
media_handovers = soma_decisoes/(max_iterations)


variancia = 0
for xi in handovers:
	variancia = variancia + (xi**2)
desvio_padrao = sqrt (variancia)
ici = media_handovers - (1.96 * (desvio_padrao/sqrt (max_iterations))) 
ics = media_handovers + (1.96 * (desvio_padrao/sqrt (max_iterations)))
media_tempo_decisao = soma_tempo / decisoes_diferente_zero
media_handovers_sem_zero = soma_decisoes / decisoes_diferente_zero
print "[LOG] Numero de erros: "+str(erros)
print "[LOG] Indices de erro: "+str(lista_erros)
for erro in lista_erros:
        intErro = int(erro)
        del handovers[intErro]
print "[LOG] Arquivo de log: "+arquivo_log
print "[LOG] Total de testes: ", str(max_iterations) 
print "[LOG] Total de handovers: ", str(soma_decisoes)
print "[LOG] Handovers: ", handovers
print "[LOG] Tempo medio total de decisoes: ", str(soma_tempo)
print "[LOG] Decisoes diferentes de zero: ", str(decisoes_diferente_zero)
print "[LOG] Media de tempo de decisoes final: ", str(media_tempo_decisao)
print "[LOG] Media de handovers: ", str(media_handovers)
print "[LOG] Media de handovers sem zeros: ", str(media_handovers_sem_zero)
print "[LOG] Variancia: ", str(variancia)
print "[LOG] Desvio padrao: ", str(desvio_padrao)
print "[LOG] Intervalo de confiancia: ["+str(ici)+", "+str(ics)+"]"
print "[LOG] Numero maximo de handovers: ", max_handovers
print "[LOG] Numero minimo de handovers: ", min_handovers
print "[LOG] Ator: ", ator
print "[LOG] Velocidade: ", velocidade

fileLog = open(arquivo_log, "w")

newText =  "######################\n"
newText = newText + "Relatorio \n"
newText = newText + "######################\n"
newText = newText + "-Ator: "+str(ator)+"\n"
newText = newText + "-Velocidade: "+str(velocidade)+"\n"
newText = newText + "-Media de decisoes por simulacao: "+str(decision/max_iterations)+"\n"
nexText = newText + "-Tempo medio total de decisoes: "+ str(soma_tempo)+"\n"
nexText = newText + "-Decisoes diferentes de zero: "+ str(decisoes_diferente_zero)+"\n"
nexText = newText + "-Media de tempo de decisoes final: "+str(media_tempo_decisao)+"\n"
newText = newText + "-Numero medio de handovers: "+str(media_handovers)+"\n"
newText = newText + "-Numero medio de handovers sem zeros: "+str(media_handovers_sem_zero)+"\n"
newText = newText + "-Numero maximo de handovers: "+str(max_handovers)+"\n"
newText = newText + "-Numero minimo de handovers: "+str(min_handovers)+"\n"
newText = newText + "-Handovers: "+ str(handovers) + "\n"
newText = newText + "-Variancia: "+ str(variancia) + "\n"
newText = newText + "-Desvio padrao: "+ str(desvio_padrao) + "\n"
newText = newText + "-Intervalo de confiancia: ["+str(ici)+", "+str(ics)+"]" + "\n"
newText = newText + "-: ["+str(ici)+", "+str(ics)+"]" + "\n"

fileLog.writelines (newText)
fileLog.close ()

