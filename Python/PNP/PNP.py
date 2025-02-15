import random
import math


registre = []
liste_simple = []
n_liste_simple = 0
liste_complete = []
operations = 0
Boss = []
classes = []

n = int(input("Veuillez entrer le nombre d'élèves: "))


triang = ((n-1)*n)/2
n_conflit = triang + 1
while n_conflit>triang:
	n_conflit = int(input("Veuillez entrer le nombre de conflits (ne doit pas dépasser " + str(triang) + " ): "))

for eleve in range(n):
	nouveau = []
	nouveau.append(str(eleve))
	nouveau.append(0)
	registre.append(nouveau)
index = 0
print()
print("Registre:")
print (registre)

while n_liste_simple < n_conflit:
	base = []
	base_2 = []
	tout = []
	
	eleve_1 = random.randint(0,n-1)
	eleve_2 = eleve_1
	while eleve_2 == eleve_1:
		eleve_2 = random.randint(0,n-1)
	
	if eleve_1 < eleve_2:
		erreurdemerde = registre[eleve_1]
		tout.append(erreurdemerde[0])
		erreurdemerde = registre[eleve_2]
		tout.append(erreurdemerde[0])
		
	else:
		erreurdemerde = registre[eleve_2]
		tout.append(erreurdemerde[0])
		erreurdemerde = registre[eleve_1]
		tout.append(erreurdemerde[0])

	
		
	
	unique = True
	for entree in liste_simple:
		
		if tout[1] == entree[1] and tout[0] == entree[0]:
			unique = False
	if unique:
		tout.append(index)
		liste_simple.append(tout)
		n_liste_simple += 1
		index +=1
print("conflits crees")
print()
print("Liste simple:")
print (liste_simple)

# A partir d'ici, toute opération doit être comptée
	
for conflit_simple in liste_simple:
	for eleve in range(n):
		operations +=1
		exist = False
		if int(conflit_simple[0]) == eleve:
			for complets in liste_complete:
				operations +=1
				if int(complets[0]) == eleve:
					exist = True
					complets.append(conflit_simple[1])
					operations +=1
					
			if not exist:
				operations +=1
				liste_complete.append([str(eleve),conflit_simple[1]])

print()
print("Liste complète:")
print (liste_complete)
					
for bosses in liste_complete:
	Boss.append(bosses[0])
	operations +=1
for eleve in registre:
	operations +=1
	if eleve[0] in Boss:
		eleve[1] += 1
print()
print("Majeurs:")
print (Boss)

for conflits in liste_complete:
	classe = []
	classe.append(conflits[0])
	operations +=1
	for eleves in registre:
		if not eleves[0] in conflits and not eleves[0] in Boss:
			classe.append(eleves[0])
			eleves[1] += 1
			operations +=1
	classes.append(classe)
	operations +=1
	
nouv_classe = []
for eleve in registre:
	operations +=1
	if eleve[1] == 0 and not eleve[0] in Boss:
		nouv_classe.append(eleve[0])
		eleve[1] += 1
		operations +=1
if nouv_classe != []:
	classes.append(nouv_classe)
	operations +=1
	
liste_taille = []
operations +=1

for classe in classes:
	operations +=1
	size = len(classe)
	info_classe = []
	info_classe.append(size)
	info_classe.append(classes.index(classe))
	liste_taille.append(info_classe)

liste_taille= sorted(liste_taille, key=lambda classe: classe[0])
operations +=1
classe_triee = []
operations +=1
for infos in liste_taille:
	operations +=1
	classe_triee.append(classes[infos[1]])
classes = classe_triee
operations +=1


print()
print("Classes non réduites:")
print (classes)

print("Nombre de classes:")
print (len(classes))
print()
print("Registre:")
print (registre)
for double in registre:
	operations +=1
	if double[1] > 1:
		operations +=1
		for classe in classes:
			operations +=1
			for eleve in classe:
				operations +=1
				if eleve == double[0] and double[1]>1:
					classe.remove(eleve)
					double[1] -= 1
					operations +=2
				
n_classes = len(classes)
while len(classes) == n_classes:
	for classe_base in classes:

		operations +=1
		if classe_base == classes[-1]:
			operations +=1
			break
		for eleve_supprimable in classe_base:
			operations +=1
			Integre = False
			for classe in reversed(classes):
				operations +=1
				Impossible = False
				if Integre == False:
					operations +=1
					for eleve in classe:
						operations +=1
						for conflit in liste_simple:
							operations +=1
							if eleve in conflit and eleve_supprimable in conflit:
								operations +=1
								Impossible = True
				else:
					operations +=1
					break
				if not Impossible:
					operations +=5
					classe.append(eleve_supprimable)
					Integre = True
					int(eleve_supprimable)
					putaindepython = registre[int(eleve_supprimable)]
					putaindepython[1] += 1
				

	n_classes = len(classes)
	for double in registre:
		operations +=1
		if double[1] > 1:
			operations +=1
			for classe in classes:
				operations +=1
				for eleve in classe:
					operations +=1
					if eleve == double[0] and double[1]>1:
						classe.remove(eleve)
						operations +=2
						double[1] -= 1

	while [] in classes:
		operations +=1
		classes.remove([])

	
print()
print("Classes après suppression des doubles, réduction, ressupression des double:")
print (classes)
print("Nombre de classes:")
print (len(classes))
print()
print("Registre:")
print (registre)




print()
print("Opérations:")
print (operations)
print()
print("Racine nème du nombre d'opérations (Si diminue en augmentant n, la résolution est polynomiale).")
print (operations**(1/n))
print("exposant de n:")
print (math.log(operations)/math.log(n))

Sol1 = classes
print("****************************************************************************")
print("fin de la solution 1")
print("Solution 2")

for eleves in registre:
	eleves[1] = 0
Boss = []
classes = []
liste_complete = []
operations = 0

for conflit_simple in reversed(liste_simple):
	for eleve in range(n):
		operations +=1
		exist = False
		if int(conflit_simple[0]) == eleve:
			for complets in liste_complete:
				operations +=1
				if int(complets[0]) == eleve:
					exist = True
					complets.append(conflit_simple[1])
					operations +=1
					
			if not exist:
				operations +=1
				liste_complete.append([str(eleve),conflit_simple[1]])

print()
print("Liste complète:")
print (liste_complete)
					
for bosses in liste_complete:
	Boss.append(bosses[0])
	operations +=1
for eleve in registre:
	operations +=1
	if eleve[0] in Boss:
		eleve[1] += 1
print()
print("Majeurs:")
print (Boss)

for conflits in liste_complete:
	classe = []
	classe.append(conflits[0])
	operations +=1
	for eleves in registre:
		if not eleves[0] in conflits and not eleves[0] in Boss:
			classe.append(eleves[0])
			eleves[1] += 1
			operations +=1
	classes.append(classe)
	operations +=1
	
nouv_classe = []
for eleve in registre:
	operations +=1
	if eleve[1] == 0 and not eleve[0] in Boss:
		nouv_classe.append(eleve[0])
		eleve[1] += 1
		operations +=1
if nouv_classe != []:
	classes.append(nouv_classe)
	operations +=1
	
liste_taille = []
operations +=1

for classe in classes:
	operations +=1
	size = len(classe)
	info_classe = []
	info_classe.append(size)
	info_classe.append(classes.index(classe))
	liste_taille.append(info_classe)

liste_taille= sorted(liste_taille, key=lambda classe: classe[0])
operations +=1
classe_triee = []
operations +=1
for infos in liste_taille:
	operations +=1
	classe_triee.append(classes[infos[1]])
classes = classe_triee
operations +=1


print()
print("Classes non réduites:")
print (classes)

print("Nombre de classes:")
print (len(classes))
print()
print("Registre:")
print (registre)
for double in registre:
	operations +=1
	if double[1] > 1:
		operations +=1
		for classe in classes:
			operations +=1
			for eleve in classe:
				operations +=1
				if eleve == double[0] and double[1]>1:
					classe.remove(eleve)
					double[1] -= 1
					operations +=2
				

for classe_base in classes:
	operations +=1
	if classe_base == classes[-1]:
		operations +=1
		break
	for eleve_supprimable in classe_base:
		operations +=1
		Integre = False
		for classe in reversed(classes):
			operations +=1
			Impossible = False
			if Integre == False:
				operations +=1
				for eleve in classe:
					operations +=1
					for conflit in liste_simple:
						operations +=1
						if eleve in conflit and eleve_supprimable in conflit:
							operations +=1
							Impossible = True
			else:
				operations +=1
				break
			if not Impossible:
				operations +=5
				classe.append(eleve_supprimable)
				Integre = True
				int(eleve_supprimable)
				putaindepython = registre[int(eleve_supprimable)]
				putaindepython[1] += 1

for double in registre:
	operations +=1
	if double[1] > 1:
		operations +=1
		for classe in classes:
			operations +=1
			for eleve in classe:
				operations +=1
				if eleve == double[0] and double[1]>1:
					classe.remove(eleve)
					operations +=2
					double[1] -= 1

while [] in classes:
	operations +=1
	classes.remove([])

	
print()
print("Classes après suppression des doubles, réduction, ressupression des double:")
print (classes)
print("Nombre de classes:")
print (len(classes))
print()
print("Registre:")
print (registre)




print()
print("Opérations:")
print (operations)
print()
print("Racine nème du nombre d'opérations (Si diminue en augmentant n, la résolution est polynomiale).")
print (operations**(1/n))
print("exposant de n:")
print (math.log(operations)/math.log(n))

Sol2 = classes
print("****************************************************************")
if len(Sol1)<len(Sol2):
	print("La meilleure solution utilise " + str(len(Sol1)) + " classes:")
	print(Sol1)
elif len(Sol1)==len(Sol2):
	print("La meilleure solution utilise " + str(len(Sol1)) + " classes:")
	print(Sol1)
	print("ou")
	print(Sol2)
else:
	print("La meilleure solution utilise " + str(len(Sol2)) + " classes:")
	print(Sol2)
