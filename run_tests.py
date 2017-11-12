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


run_commands = [
    "./run ~/Downloads/Zlatoust.ppm",
    "./run ~/Downloads/teamviewer_12.0.85001_i386.deb",
    "./run ~/Downloads/NVIDIA-Linux-x86_64-375.66.run",
    "./run ~/Downloads/netbeans-8.2-linux.sh",
    "./run ~/Downloads/debian-9.1.0-i386-xfce-CD-1.iso",
    "./run ~/Downloads/lubuntu-17.04-desktop-i386.iso",
    "./run_gpu ~/Downloads/Zlatoust.ppm",
    "./run_gpu ~/Downloads/teamviewer_12.0.85001_i386.deb",
    "./run_gpu ~/Downloads/NVIDIA-Linux-x86_64-375.66.run",
    "./run_gpu ~/Downloads/netbeans-8.2-linux.sh",
    "./run_gpu ~/Downloads/debian-9.1.0-i386-xfce-CD-1.iso",
    "./run_gpu ~/Downloads/lubuntu-17.04-desktop-i386.iso"
]
files_names = [
    "Zlatoust.ppm",
    "teamviewer_12.0.85001_i386.deb",
    "NVIDIA-Linux-x86_64-375.66.run",
    "netbeans-8.2-linux.sh",
    "debian-9.1.0-i386-xfce-CD-1.iso",
    "lubuntu-17.04-desktop-i386.iso",
    "Zlatoust.ppm",
    "teamviewer_12.0.85001_i386.deb",
    "NVIDIA-Linux-x86_64-375.66.run",
    "netbeans-8.2-linux.sh",
    "debian-9.1.0-i386-xfce-CD-1.iso",
    "lubuntu-17.04-desktop-i386.iso"
]
#os.system("rm -f -r output_tests/*")
rodadas = 5
#for idx, cmd in enumerate(run_commands):
#  tipo = "cpu"
#  if idx >= 6:
#    tipo = "gpu"
#  for i in range(0, rodadas):
#    r = os.system(cmd + " > output_tests/" + tipo + "_" + str(idx) + "_" + str(i))
#    if r == 2:
#      print "Programa fechado por CTRL + C"
#      exit(2)
res = []
tam = []
for idx, cmd in enumerate(run_commands):
  tipo = "cpu"
  if idx >= 6:
    tipo = "gpu"
  res_p = []
  for i in range(0, rodadas):
    f = open("output_tests/" + tipo + "_" + str(idx) + "_" + str(i), 'r')
    spl = f.readline().split('|')
    s = spl[0]
    t = spl[1]
    if i == 0:
      tam.insert(idx, float(s))
    res_p.insert(i, float(t[:len(t) - 1]))
  res.insert(idx, res_p)

matriz_saida = []
for idR, r in enumerate(res):
  tp = mean_confidence_interval(r, 0.95)
  matriz_saida.insert(idx * 3, tp[0])
  matriz_saida.insert(idx * 3 + 1, tp[1])
  matriz_saida.insert(idx * 3 + 2, tp[2])

for i in range(0, 6):
  print "## " + str(matriz_saida[i * 3]) + " " + str(matriz_saida[i * 3 + 1]) + " " + str(matriz_saida[i * 3 + 2]) + " ",
  print str(matriz_saida[18 + (i * 3)]) + " " + str(matriz_saida[18 + (i * 3) + 1]) + " " + str(matriz_saida[18 + (i * 3) + 2])
  #m = np.mean(r)
  #print tam[idR] / m
