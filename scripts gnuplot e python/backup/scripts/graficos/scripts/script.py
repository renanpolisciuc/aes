import os
import sys


print "[LOG] Gerando graficos...",
i = 1
while i < 12:
	os.system ("gnuplot "+str(i)+".gnu")
	i = i + 1

print "done."
