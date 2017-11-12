import os
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
os.system("rm -f -r output_tests/*")
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

for idx, cmd in enumerate(run_commands):
  tipo = "cpu"
  if idx >= 6:
    tipo = "gpu"
  for i in range(0, rodadas):
    nome_arquivo = "output_tests/" + tipo + "_" + str(idx) + "_" + str(i)
    print nome_arquivo
