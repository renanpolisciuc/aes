from os import listdir
from os.path import isfile, isdir, join

currentFolder = "."
folders = [ f for f in listdir(currentFolder) if isdir(join(currentFolder,f)) and f[0] == 'l' ]
countFolders = len(folders)

for folder in folders: 
	filesInFolder = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
	countDecisions = 0
	countFiles = 0
	for fileInFolder in filesInFolder:
		fOpen = open (folder+"/"+fileInFolder, "r")
		fLines = fOpen.readlines ()
		countDecision = 0
		for line in fLines:
			if line.find ("DecisionModule:Run") > -1:
				countDecision = countDecision +1
		print "[LOG] ("+folder+"/"+fileInFolder+") => Numero de decisoes: "+str(countDecision)
		countDecisions = countDecisions + countDecision
		countFiles = countFiles + 1
		fOpen.close ()
	print "[LOG] ("+folder+") => Numero de Arquivos: "+str (countFiles) + "/ Numero de decisoes: "+ str (countDecisions) + " / Media: "+str (countDecisions/30)
print "[LOG] Numero de pastas: " + str (countFolders)
