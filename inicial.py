from os import walk
import os
import shutil


f = []
for (dirpath, dirnames, filenames) in walk("C:/Users/user/Desktop/PROJETO/ARQUIVOS"):
    for file in filenames:
    	f.append(file)

i = 0
print("Quantidade de arquivos encontrados:", +len(f) , "\n")
while i < len(f):	
	print (f[i].replace("\\","/"))
	os.rename('C:/Users/user/Desktop/PROJETO/ARQUIVOS/'+f[i] , 'C:/Users/user/Desktop/PROJETO/ARQUIVOS/OUTPUT/'+f[i].replace(".txt",".hql"))
	print ('resultado')
	print (f[i])
	i += 1

	print("Isso é um outro teste")

