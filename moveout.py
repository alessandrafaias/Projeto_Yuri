from os import walk
import os
#import shutil
import re

f = []
for (dirpath, dirnames, filenames) in walk("C:/Users/user/Desktop/PROJETO/OUTPUT"):
    for file in filenames:
    	f.append(file)

print ("Listando arquivos a serem transferidos \n")
print (dirpath, f)
print("\nQuantidade de arquivos encontrados:", +len(f) , "\n")
i = 0
while i < len(f):	
	os.rename('C:/Users/user/Desktop/PROJETO/OUTPUT/'+f[i] , 'C:/Users/user/Desktop/PROJETO/ARQUIVOS/'+f[i].replace(".hql",".txt"))
	#print ('resultado')
	#print (f[i])
	i += 1
fd = []
for (dirpath, dirnames, filenames) in walk("C:/Users/user/Desktop/PROJETO/ARQUIVOS"):
    for file in filenames:
    	fd.append(file)


print ("Listando arquivos após transferência \n")
print (dirpath, fd)