from os import walk
import os
import re

#Variáveis
dir_origem = "C:/Users/user/Desktop/PROJETO/ARQUIVOS/"
search = 'ale'
change = 'alexandra'

#Concatenando os nomes dos arquivos no vetor
nome= ''
fd = []
f = []
for (dirpath, dirnames, filenames) in walk(dir_origem):
    for file in filenames:
    	f.append(file)

print ("\nArquivos encontrados: \n")
print (dirpath, f)
print("\nQuantidade de arquivos encontrados:", +len(f) , "\n")

#Compara os arquivos com a variável search
#Se for igual, o nome é alterado de acordo com a variável change
i = 0
while i < len(f):
	#Separa o nome e a extensão, e guarda em um vetor
	arquivo = os.path.splitext(f[i]) 
	print (arquivo[0])
	#Compara se o nome do arquivo começa com 'ale' (conteúdo da variável search)
	comparacao = re.compile(search).match
	if comparacao(arquivo[0]):
		if arquivo[0] != change:
			os.rename(dir_origem+f[i] , dir_origem+change+arquivo[1])
			nome = arquivo[0]+arquivo[1]
			nome_alterado = change+arquivo[1]
			fd.append(nome_alterado)
	i += 1
#Verifica se algum arquivo foi ou não alterado
if nome != '':
	print ("\nArquivos alterados: ")
	print (dirpath, 'de ', nome, ' para ', fd)
else:
	print ("\nNenhum arquivo foi alterado!")