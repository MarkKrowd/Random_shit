import random


#Création des villes
N = int(input("Entrez le nombre de villes à visiter: "))

#Les villes sont numérotées de 0 à n dans un registre (0,0),(1,0),...,(n,0) le zéro correspond au nombre de fois où la ville a été visitée.

Registre = []
for ville in range(N):
	new = [ville,0]
	Registre.append(new)
	
print (Registre)

#La distance séparant chaque ville est maintenant créée (aléatoirement et arbitrairement de 1000 à 100000m), considérant que les chemins n'allant pas forcément tout droit d'une ville à l'autre, il n'y a pas de restriction géométrique)

Carte = []

for ville_1 in Registre:
	num_ville_1 = ville_1[0]
	fini = False
	for ville_2 in Registre[:-1]:
		num_ville_2 = ville_2[0]
		if not fini:
			if num_ville_1 == num_ville_2:
				fini = True
			else:
				#changer la plage de distance entre les villes ici
				distance = random.randint(1,100000)
				chemin = [distance,num_ville_1,num_ville_2]
				Carte.append(chemin)
Carte = sorted(Carte)			
print (Carte)

#Essai de chemins en partant d'une ville et en prenant les chemins les lus courts

print("Méthode polynomiale:")

for ville_depart in Registre:
	Longueur = 0
	Carnet = []
	for vidange in Registre:
		vidange[1] = 0
	ville_depart[1] += 1
	for route in Carte:
		ville_1 = Registre[route[1]]
		ville_2 = Registre[route[2]]
		if ville_1[1]<2 and ville_2[1]<2:
			Itin = [ville_1[0],ville_2[0]]
			Longueur += route[0]
			ville_1[1]+=1
			ville_2[1]+=1
			Carnet.append(Itin)
	print("Ville de départ: " + str(ville_depart[0]) + ", Carnet de voyage: " + str(Carnet) + ", Longueur = " + str(Longueur) + "m")
	
print("Méthode exponentielle:")

def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)


		
for ville_depart in Registre:
	
	Possibilites = []
	vide = 0
	nombre = fact(N-1)
	for chemin in range(nombre):
		Possibilites.append(vide)
	
	
	
	
	
	print(Possibilites)
	
