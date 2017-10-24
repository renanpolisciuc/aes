import os
import sys

#Numero minimo de parametros
if len(sys.argv) < 8:
	print "Faltam argumentos!"
	print "Help: python filter.py [pasta] [prefix] [extension] [pattern1],[patter2],...,[patterN] [iteracoes] [pasta de saida] [prefixo de saida]"
	exit(-1)

#pasta dos logs
foldername = sys.argv[1]
foldernameOut = sys.argv[6]

#Nome do arquivo
filename = sys.argv[2]

#extensao do arquivo
extension = sys.argv[3]

#String do filtro
filterString = sys.argv[4]
patterns = filterString.split (",")


#Contador de leituras
counter = 0

#numero de iteracoes
iteracoes = int(sys.argv[5])

print "[LOG]: Pasta de logs: ", foldername
print "[LOG]: Prefixo de entrada: ", filename
print "[LOG]: Arquivos de saida: ", foldernameOut+"/"+sys.argv[7]+"X.out"
print "[LOG]: Strings de filtro: ", patterns
print "[LOG]: Numero de iteracoes: ", iteracoes

clean = os.system("rm -r "+foldernameOut+"*")
print "[LOG] Clean: ", clean
if clean <> 0:
	os.system("mkdir "+foldernameOut)	

#executa o numero de arquivos
while counter < iteracoes :
	print "[LOG] Filtrando arquivo: ", foldername+filename+str(counter)+extension," => "+foldernameOut+sys.argv[7]+str(counter)+".out",
        #Abre o arquivo
	fileIn = open(foldername+filename+str(counter)+extension, "r")
	
        #Le todas as linhas do arquivo
	lines = fileIn.readlines ()
	
	#abre o arquivo de saida
	fileOut = open (foldernameOut+sys.argv[7]+str(counter)+".out", "w+")

        fileOut.write ("#Arquivo "+str(counter)+"\n")
	
        #percorre linha a linha
	for line in lines:
		for pattern in patterns:
			if line.find (pattern) > -1 :
				fileOut.write (line)
        
	fileOut.write ("#FimArquivo"+str(counter)+"\n\n")

        #Fecha o arquivo
	fileIn.close()
	print "done."
	
	#fecha o arquivo de saida
	fileOut.close ()

	#aumenta o contador
	counter = counter + 1
		
