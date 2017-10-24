#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ^^^ Permite utilização de utf8 ^^^

# Bibliotecas básicas
import glob
import sys
import os

print "[LOG] Obtendo nome dos arquivos gnuplot."

# Obtém todos os arquivos de extensão .gnu da posta corrente e coloca numa lista
allFilesGnu = glob.glob ("*.gnu")
print "[LOG] Lista de arquivos gnuplot gerada."

print "[LOG] Executando arquivos gnuplot."

# Percorre a lista
for eachFile in allFilesGnu:
	print "[LOG] Executando "+eachFile

	# Comando que será executado
	command = "gnuplot "+eachFile
	print "Shell command => "+command

	# Executa o comando no shell
	result = os.system (command)

	# ERRO
	if result == 256:
		print "[LOG] Erro no arquivo: "+eachFile
		exit (1)	
