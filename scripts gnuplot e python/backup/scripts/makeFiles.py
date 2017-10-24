import os
import sys


folder = "log"
prefixLogExec = ['lc', 'lm', 'lp']
prefixLogTime = ['tc', 'tm', 'tp']
prefixLogCont = ['cc', 'cm', 'cp']

numberOfNetworks = ['2', '10', '20']
intervalDecision = ['10', '15', '20']

sufixFinalLog = '_log'

#criando diretorio principal
os.system ("rm -r scripts/"+folder+"/")
print "[LOG] Criando diretorio => scripts/"+folder
os.system("mkdir scripts/"+folder)

#criando diretorios de log
for ple in prefixLogExec:
	for non in numberOfNetworks:
		for ind in intervalDecision:
			print "[LOG] Criando diretorio => scripts/"+folder+"/"+ple+non+ind
			os.system("mkdir scripts/"+folder+"/"+ple+non+ind)
                        
			
			print "[LOG] Criando arquivo => scripts/"+ple+non+ind+sufixFinalLog
			os.system("touch scripts/out/"+ple+non+ind+sufixFinalLog)

#criando diretorios de tempo
for plt in prefixLogTime:
	for non in numberOfNetworks:
		for ind in intervalDecision:
			print "[LOG] Criando diretorio => scripts/"+folder+"/"+plt+non+ind
			os.system("mkdir scripts/"+folder+"/"+plt+non+ind)

#criando diretorios de contagem
for plc in prefixLogCont:
	for non in numberOfNetworks:
		for ind in intervalDecision:
			print "[LOG] Criando diretorio => scripts/"+folder+"/"+plc+non+ind
			os.system("mkdir scripts/"+folder+"/"+plc+non+ind)
