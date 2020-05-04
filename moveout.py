from os import walk
import os
import re

#Variáveis
dir_origem = "C:/Users/user/Desktop/PROJETO/OUTPUT/"
dir_destino = "C:/Users/user/Desktop/PROJETO/ARQUIVOS/"
ext = ".hql"
new_ext = ".txt"

#Concatenando os nomes dos arquivos no vetor
f = []
for (dirpath, dirnames, filenames) in walk(dir_origem):
    for file in filenames:
    	f.append(file)

print ("Arquivos a serem transferidos: \n")
print (dirpath, f)
print("\nQuantidade de arquivos encontrados:", +len(f) , "\n")

#Compara a extensão do arquivo e muda de diretório
i = 0
while i < len(f):
	arquivo = os.path.splitext(f[i])
	if arquivo[1] != new_ext:
		nf = arquivo[0] + new_ext
		os.rename(dir_origem+f[i] , dir_destino+nf)
	i += 1

#Lista os arquivos movidos
fd = []
for (dirpath, dirnames, filenames) in walk(dir_destino):
    for file in filenames:
    	fd.append(file)

print ("Arquivos após transferência: \n")
print (dirpath, fd)