a1 = open("resultado_blast_transposonxgenoma_qstart", "r")
a2 = open("resultado_blast_transposonxgenoma_qend", "r")
a3 = open("inicio_gff3","r")
a4 = open("final_gff3","r")

qstart = []
qend = []
inicio = []
fim = []


for linha in a1:
	qstart.append((linha))      
for linha in a2:                                      
	qend.append((linha))

for linha in a3:
	inicio.append(linha)      
for linha in a4:                                      
	fim.append(linha)

tupla = zip(qstart, qend)
tupla2 = zip(inicio, fim)


a1.close()
a2.close()
a3.close()
a4.close()

fora_antes = 0
parcial_antes = 0
dentro = 0
parcial_depois = 0
fora_depois = 0


for inicio, fim in tupla2:
	for qstart, qend in tupla:
		if  qend <= inicio:
			fora_antes += 1
		elif qstart <= inicio and qend >= fim:
			parcial_antes += 1
		elif qstart >= inicio and qend <= fim:
			dentro += 1
		elif qstart >= inicio and qend >= fim:
			parcial_depois += 1 
		elif qstart >= fim:
			fora_depois += 1  

print fora_antes, parcial_antes, dentro, parcial_depois, fora_depois






