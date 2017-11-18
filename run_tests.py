import os
import numpy as np
import scipy as sp
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
  a = 1.0*np.array(data)
  n = len(a)
  m, se = np.mean(a), scipy.stats.sem(a)
  h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
  return m, m-h, m+h

def calcularTamanho(tamanho):
  temp = float(tamanho) * 1000
  if (temp < 1):
    return str(int((temp * 1000))) + "KB"
  return str(int(temp)) + "MB"

pasta_amostra = "amostras"
pasta_saida = "output_tests/"
runtimes = ["./run", "./run_gpu"]
tp_run = ["cpu", "gpu"]
rodadas = 20

arqs = [f for f in os.listdir(pasta_amostra) if os.path.isfile(os.path.join(pasta_amostra, f))]

arqs_o = []
for a in arqs:
  l = os.path.join(pasta_amostra, a)
  s = os.path.getsize(l)
  arqs_o.append((s, a))
arqs_o.sort(key=lambda s: s[0])

count_arqs_saida = len(os.listdir(pasta_saida))
if count_arqs_saida == 0:
  for ri, run in enumerate(runtimes):
    for fi, f in enumerate(arqs_o):
      for it in range(0, rodadas):
        arq_saida = pasta_saida + tp_run[ri] + "_" + str(fi) + "_" + str(it)
        cmd = run + " " + pasta_amostra + "/"+ f[1] + " > " + arq_saida
        run_code = os.system(cmd)
        if run_code == 2:
          print "Programa fechado por CTRL + C"
          exit(2)
res = []
tam = []
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
matriz_saida = []
for idR, r in enumerate(res):
  tp = mean_confidence_interval(r, 0.95)
  matriz_saida.insert(idR, tp)

len_arqs = len(arqs_o)
for i in range(0, len_arqs):
  c1 = float(tam[i] / matriz_saida[i][0])
  c2 = float(tam[i] / matriz_saida[i][1])
  c3 = float(tam[i] / matriz_saida[i][2])
  g1 = float(tam[i] / matriz_saida[i + len_arqs][0])
  g2 = float(tam[i] / matriz_saida[i + len_arqs][1])
  g3 = float(tam[i] / matriz_saida[i + len_arqs][2])
  print str(calcularTamanho(tam[i])) + " " + str(c1) + " " + str(c2) + " " + str(c3) + " ",
  print str(g1) + " " + str(g2) + " " + str(g3)
  #m = np.mean(r)
  #print tam[idR] / m

#for i in range(0, 6):
#  c1 = float(tam[i] / matriz_saida[i * 3])
#  c2 = float(tam[i] / matriz_saida[i * 3 + 1])
#  c3 = float(tam[i] / matriz_saida[i * 3 + 2])
#  g1 = float(tam[i + 6] / matriz_saida[18 + (i * 3)])
#  g2 = float(tam[i + 6] / matriz_saida[18 + (i * 3) + 1])
#  g3 = float(tam[i + 6] / matriz_saida[18 + (i * 3) + 2])
#  print str(calcularTamanho(tam[i])) + " " + str(c1) + " " + str(c2) + " " + str(c3) + " ",
#  print str(g1) + " " + str(g2) + " " + str(g3)
#  #m = np.mean(r)
#  #print tam[idR] / m
