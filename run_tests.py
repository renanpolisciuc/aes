#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import scipy as sp
import scipy.stats

#Método que calcula o intervalo de confiança
def mean_confidence_interval(data, confidence=0.95):
  a = 1.0*np.array(data)
  n = len(a)
  m, se = np.mean(a), scipy.stats.sem(a)
  h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
  return m, m-h, m+h

#Obtém o tamanho do arquivo em Megas ou KBytes
def calcularTamanho(tamanho):
  temp = float(tamanho) * 1000
  if (temp < 1):
    return str(int((temp * 1000))) + "KB"
  return str(int(temp)) + "MB"

#Pasta padrão com as amostras
pasta_amostra = "amostras"

#Pasta de saída
pasta_saida = "output_tests/"

#Programas de CPU e GPU
runtimes = ["./run", "./run_gpu"]

#Tipos
tp_run = ["cpu", "gpu"]

#Número de simulações por arquivo
rodadas = 20

#Obtém os arquivos da pasta de amostras
arqs = [f for f in os.listdir(pasta_amostra) if os.path.isfile(os.path.join(pasta_amostra, f))]

#Ordena a lista de arquivos pelo tamanho
arqs_o = []
for a in arqs:
  l = os.path.join(pasta_amostra, a)
  s = os.path.getsize(l)
  arqs_o.append((s, a))
arqs_o.sort(key=lambda s: s[0])

#Conta o número de arquivos de saída
count_arqs_saida = len(os.listdir(pasta_saida))

#Se não tiverem arquivos de saída, simula novamente
if count_arqs_saida == 0:

  # programa x arquivo x rodadas
  for ri, run in enumerate(runtimes):
    for fi, f in enumerate(arqs_o):
      for it in range(0, rodadas):

        arq_saida = pasta_saida + tp_run[ri] + "_" + str(fi) + "_" + str(it)
        cmd = run + " " + pasta_amostra + "/"+ f[1] + " > " + arq_saida

        #Executa o comando shell
        run_code = os.system(cmd)

        #Finaliza o programa se o usuário der CTRL + C
        if run_code == 2:
          print "Programa fechado por CTRL + C"
          exit(2)

#Resultados(tempos)
res = []

#Tamanhos dos arquivo
tam = []

#Obtém os tempos e tamanhos dos arquivos
#A saída dos programas "tamanho em bytes | tempo em milisegundos "
for ri, run in enumerate(runtimes):
  for fi, f in enumerate(arqs_o):
    res_p = []
    for it in range(0, rodadas):
      f = open(pasta_saida + tp_run[ri] + "_" + str(fi) + "_" + str(it), 'r')
      spl = f.readline().split('|')
      t = spl[1]
      s = spl[0]
      if ri == 0 and it == 0:
        tam.append(float(s))
      res_p.insert(it, float(t[:len(t) - 1]))
    res.insert(ri * len(arqs_o) + fi, res_p)

#Calcula os resultados médios e os intervalos de confiança por arquivo
matriz_saida = []
for idR, r in enumerate(res):
  tp = mean_confidence_interval(r, 0.95)
  matriz_saida.insert(idR, tp)

#Conta o número de arquivos de entrada
len_arqs = len(arqs_o)

#Gera a saída para o gráfico de velocidades
f_vel = open("graficos/velocidades.txt", 'w')
for i in range(0, len_arqs):
  c1 = float(tam[i] / matriz_saida[i][0])
  c2 = float(tam[i] / matriz_saida[i][1])
  c3 = float(tam[i] / matriz_saida[i][2])
  g1 = float(tam[i] / matriz_saida[i + len_arqs][0])
  g2 = float(tam[i] / matriz_saida[i + len_arqs][1])
  g3 = float(tam[i] / matriz_saida[i + len_arqs][2])

  f_vel.write(str(calcularTamanho(tam[i])) + " " + str(c1) + " " + str(c2) + " " + str(c3) + " " + str(g1) + " " + str(g2) + " " + str(g3) + "\n")
f_vel.close()
#Gera a saída para o gráfico de speedup
f_speedup = open("graficos/speedup.txt", 'w')
for i in range(0, len_arqs):
  c1 = float(tam[i] / matriz_saida[i][0])
  c2 = float(tam[i] / matriz_saida[i][1])
  c3 = float(tam[i] / matriz_saida[i][2])
  g1 = float(tam[i] / matriz_saida[i + len_arqs][0])
  g2 = float(tam[i] / matriz_saida[i + len_arqs][1])
  g3 = float(tam[i] / matriz_saida[i + len_arqs][2])
  f_speedup.write(str(calcularTamanho(tam[i])) + " " + str(g1 / c1) + " " + str(g2 / c2) + " " + str(g3 / c3) + "\n")
f_speedup.close()
os.system("gnuplot graficos/velocidades.gnu")
os.system("gnuplot graficos/speedup.gnu")
os.system("evince graficos/velocidades.eps")
os.system("evince graficos/speedup.eps")
