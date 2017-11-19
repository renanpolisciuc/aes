#!/bin/bash
FILES[0]="/home/renan/Downloads/Zlatoust.ppm"
FILES[1]="/home/renan/Downloads/teamviewer_12.0.85001_i386.deb"
FILES[2]="/home/renan/Downloads/NVIDIA-Linux-x86_64-375.66.run"
FILES[3]="/home/renan/Downloads/netbeans-8.2-linux.sh"
FILES[4]="/home/renan/Downloads/debian-9.1.0-i386-xfce-CD-1.iso"
FILES[5]="/home/renan/Downloads/lubuntu-17.04-desktop-i386.iso"

for file in "${FILES[@]}"
do
  ls -l -h -s $file | cut -d' ' -f1
done
