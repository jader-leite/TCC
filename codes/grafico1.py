a1 = open("qstart", "r")
a2 = open("qend", "r")

#qstart = a1.readlines()
#for i in len(qstart):
#	qstart[i] = int(qstart[i])         #a ideia aqui era pegar os arquivos quebrar ele em uma lista de strings e transformar os elementos de string para int
#qend = a2.readlines()                            ####NAO FUNFOU####
#for i in len(qend):
#	qend[i] = int(qend[i])

qstart = []
qend = []

for linha in a1:
	qstart.append(int(linha))      #a segunda ideia eh abrir duas listas e ir transformando a str em int e adicionando ao final da lista
for linha in a2:                                      ####FUNFOU####
	qend.append(int(linha))


tupla = zip(qstart, qend)

a1.close()
a2.close() 


#AGORA COM A TUPLA EU CONSIGO FAZER UM CONDICIONAL PARA COMPARAR####

grafico = []
count = 0 #contador que vai indicar o indice da lista para fazer o eixo y do grafico
valor = 0 #vai pegar o valor e vai comparar com o qstart e qend para ver se esta ali

for i in range (len(tupla)):
	for qstart, qend in tupla:
		if valor >= qstart and valor <= qend:
			count += 1	
	grafico.append(count)
	valor += 1
	count = 0

#print grafico

a3 = open("grafico", "w")

for j in grafico:
	a3.write(str(j))
	a3.write("\n")

a3.close()
