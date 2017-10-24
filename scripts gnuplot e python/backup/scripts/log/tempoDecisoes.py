from os import listdir
from os.path import isfile, isdir, join

currentFolder = "."
folders = [ f for f in listdir(currentFolder) if isdir(join(currentFolder,f)) and f[0] == 't' ]
countFolders = len(folders)


tempo_2_10  = 0
tempo_2_15  = 0
tempo_2_20  = 0
tempo_10_10 = 0
tempo_10_15 = 0
tempo_10_20 = 0
tempo_20_10 = 0
tempo_20_15 = 0
tempo_20_20 = 0

n_pastas_2_10  = 0
n_pastas_2_15  = 0
n_pastas_2_20  = 0
n_pastas_10_10 = 0
n_pastas_10_15 = 0
n_pastas_10_20 = 0
n_pastas_20_10 = 0
n_pastas_20_15 = 0
n_pastas_20_20 = 0

tempos_2_10 = []
tempos_2_15 = []
tempos_2_20 = []
tempos_10_10 = []
tempos_10_15 = []
tempos_10_20 = []
tempos_20_10 = []
tempos_20_15 = []
tempos_20_20 = []
for folder in folders: 
	filesInFolder = [ f for f in listdir(folder) if isfile(join(folder,f)) ]


	countDecisions = 0
	countFiles = 0
	soma_media_tempo = 0
	for fileInFolder in filesInFolder:
		fOpen = open (folder+"/"+fileInFolder, "r")
		fLines = fOpen.readlines ()
		
		countDecision = 0
		tempo_decisao = 0
		for line in fLines:
			if line.find ("Decision") > -1 :
				countDecision = countDecision + 1
				find = line.find ("Miliseconds:")
				if find > -1:
					tempo = int(line[find+len("Miliseconds:")+1::])
					tempo_decisao = tempo_decisao + tempo
#					print "[LOG] ("+folder+"/"+fileInFolder+") Tempo: "+ str(int(line[find+len("Miliseconds:")+1::]))
							
		if countDecision <> 0:
			media_tempo = tempo_decisao/countDecision
		else:
			media_tempo = 0
		soma_media_tempo = soma_media_tempo + media_tempo			
#		print "[LOG] ("+folder+"/"+fileInFolder+") => Numero de decisoes: "+str(countDecision)+" / Tempo de decisao total: "+ str(tempo_decisao) +" / Tempo medio de decisao: "+str(media_tempo)
		countDecisions = countDecisions + countDecision
		countFiles = countFiles + 1
		fOpen.close ()

	if folder[2] == '2' and folder[3] <> '0':
		if folder[3:] == '10':
			n_pastas_2_10 = n_pastas_2_10 + 1
			tempo_2_10 = tempo_2_10 + (soma_media_tempo/countFiles)
			tempos_2_10.append (soma_media_tempo/countFiles)
		elif folder[3:] == '15':
			n_pastas_2_15 = n_pastas_2_15 + 1
			tempo_2_15 = tempo_2_15 + (soma_media_tempo/countFiles)
			tempos_2_15.append (soma_media_tempo/countFiles)
		else:
			n_pastas_2_20 = n_pastas_2_20 + 1
			tempo_2_20 = tempo_2_20 + (soma_media_tempo/countFiles)
			tempos_2_20.append (soma_media_tempo/countFiles)
	elif folder[2] == '2' and folder[3] == '0':
		if folder[4:] == '10':
			n_pastas_20_10 = n_pastas_20_10 + 1
			tempo_20_10 = tempo_20_10 + (soma_media_tempo/countFiles)
			tempos_20_10.append (soma_media_tempo/countFiles)
		elif folder[4:] == '15':
			n_pastas_20_15 = n_pastas_20_15 + 1
			tempo_20_15 = tempo_20_15 + (soma_media_tempo/countFiles)
			tempos_20_15.append (soma_media_tempo/countFiles)
		else:
			n_pastas_20_20 = n_pastas_20_20 + 1
			tempo_20_20 = tempo_20_20 + (soma_media_tempo/countFiles)
			tempos_20_20.append (soma_media_tempo/countFiles)
	else:
		if folder[4:] == '10':
			n_pastas_10_10 = n_pastas_10_10 + 1
			tempo_10_10 = tempo_10_10 + (soma_media_tempo/countFiles)
			tempos_10_10.append (soma_media_tempo/countFiles)
		elif folder[4:] == '15':
			n_pastas_10_15 = n_pastas_10_15 + 1
			tempo_10_15 = tempo_10_15 + (soma_media_tempo/countFiles)
			tempos_10_15.append (soma_media_tempo/countFiles)
		else:
			n_pastas_10_20 = n_pastas_10_20 + 1
			tempo_10_20 = tempo_10_20 + (soma_media_tempo/countFiles)
			tempos_10_20.append (soma_media_tempo/countFiles)

	print "[LOG] ("+folder+") => Numero de Arquivos: "+str (countFiles) + "/ Numero de decisoes: "+ str (countDecisions) + " / Media de tempo: "+str (soma_media_tempo/countFiles)
print "[LOG] Numero de pastas: " + str (countFolders)
print "[LOG] Numero de pastas de 2-10 redes: " + str (n_pastas_2_10)
print "[LOG] Numero de pastas de 2-15 redes: " + str (n_pastas_2_15)
print "[LOG] Numero de pastas de 2-20 redes: " + str (n_pastas_2_20)
print "[LOG] Numero de pastas de 2 redes: " + str (n_pastas_2_10+n_pastas_2_15+n_pastas_2_20)
print "[LOG] Numero de pastas de 10-10 redes: " + str (n_pastas_10_10)
print "[LOG] Numero de pastas de 10-15 redes: " + str (n_pastas_10_15)
print "[LOG] Numero de pastas de 10-20 redes: " + str (n_pastas_10_20)
print "[LOG] Numero de pastas de 10 redes: " + str (n_pastas_10_10+n_pastas_10_15+n_pastas_10_20)
print "[LOG] Numero de pastas de 20-10 redes: " + str (n_pastas_20_10)
print "[LOG] Numero de pastas de 20-15 redes: " + str (n_pastas_20_15)
print "[LOG] Numero de pastas de 20-20 redes: " + str (n_pastas_20_20)
print "[LOG] Numero de pastas de 20 redes: " + str (n_pastas_20_10+n_pastas_20_15+n_pastas_20_20)
print "[LOG] Tempos medios de 2-10 redes: " + str (tempos_2_10)
print "[LOG] Tempos medios de 2-15 redes: " + str (tempos_2_15)
print "[LOG] Tempos medios de 2-20 redes: " + str (tempos_2_20)
print "[LOG] Tempos medios de 2 redes: " + str (tempos_2_10 + tempos_2_15 + tempos_2_20)
print "[LOG] Tempos medios de 10-10 redes: " + str (tempos_10_10)
print "[LOG] Tempos medios de 10-15 redes: " + str (tempos_10_15)
print "[LOG] Tempos medios de 10-20 redes: " + str (tempos_10_20)
print "[LOG] Tempos medios de 10 redes: " + str (tempos_10_10 + tempos_10_15 + tempos_10_20)
print "[LOG] Tempos medios de 20-10 redes: " + str (tempos_20_10)
print "[LOG] Tempos medios de 20-15 redes: " + str (tempos_20_15)
print "[LOG] Tempos medios de 20-20 redes: " + str (tempos_20_20)
print "[LOG] Tempos medios de 20 redes: " + str (tempos_20_10 + tempos_20_15 + tempos_20_20)
print "[LOG] Tempo total de 2-10 redes: " + str (tempo_2_10)
print "[LOG] Tempo total de 2-15 redes: " + str (tempo_2_15)
print "[LOG] Tempo total de 2-20 redes: " + str (tempo_2_20)
print "[LOG] Tempo total de 2 redes: " + str (tempo_2_10 + tempo_2_15 + tempo_2_20)
print "[LOG] Tempo total de 10-10 redes: " + str (tempo_10_10)
print "[LOG] Tempo total de 10-15 redes: " + str (tempo_10_15)
print "[LOG] Tempo total de 10-20 redes: " + str (tempo_10_20)
print "[LOG] Tempo total de 10 redes: " + str (tempo_10_10 + tempo_10_15 + tempo_10_20)
print "[LOG] Tempo total de 20-10 redes: " + str (tempo_20_10)
print "[LOG] Tempo total de 20-15 redes: " + str (tempo_20_15)
print "[LOG] Tempo total de 20-20 redes: " + str (tempo_20_20)
print "[LOG] Tempo total de 20 redes: " + str (tempo_20_10 + tempo_20_15 + tempo_20_20)
print "[LOG] Media de tempo de 2 redes: " + str ( (tempo_2_10 + tempo_2_15 + tempo_2_20) / (n_pastas_2_10 + n_pastas_2_15 + n_pastas_2_20) )
print "[LOG] Media de tempo de 2-10 redes: " + str ( (tempo_2_10) / (n_pastas_2_10) )
print "[LOG] Media de tempo de 2-15 redes: " + str ( (tempo_2_15) / (n_pastas_2_15) )
print "[LOG] Media de tempo de 2-20 redes: " + str ( (tempo_2_20) / (n_pastas_2_20) )
print "[LOG] Media de tempo de 10 redes: " + str ( (tempo_10_10 + tempo_10_15 + tempo_10_20) / (n_pastas_10_10 + n_pastas_10_15 + n_pastas_10_20) )
print "[LOG] Media de tempo de 10-10 redes: " + str ( (tempo_10_10) / (n_pastas_10_10) )
print "[LOG] Media de tempo de 10-15 redes: " + str ( (tempo_10_15) / (n_pastas_10_15) )
print "[LOG] Media de tempo de 10-20 redes: " + str ( (tempo_10_20) / (n_pastas_10_20) )
print "[LOG] Media de tempo de 20 redes: " + str ( (tempo_20_10 + tempo_20_15 + tempo_20_20) / (n_pastas_20_10 + n_pastas_20_15 + n_pastas_20_20) )
print "[LOG] Media de tempo de 20-10 redes: " + str ( (tempo_20_10) / (n_pastas_20_10) )
print "[LOG] Media de tempo de 20-15 redes: " + str ( (tempo_20_15) / (n_pastas_20_15) )
print "[LOG] Media de tempo de 20-20 redes: " + str ( (tempo_20_20) / (n_pastas_20_20) )
