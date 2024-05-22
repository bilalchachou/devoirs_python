#------------------------------------------1---------------------------------------------------

tables = [1, 2, 3, 5, 8]

resultats_multiplications = [[table * multiplicateur for multiplicateur in range(1, 11)] for table in tables]

for i, table in enumerate(tables):
    print(f"Table de multiplication de {table}: {resultats_multiplications[i]}")
    
#------------------------------------------2---------------------------------------------------

nombres = [str(i) for i in range(1, 11)]

resultats = []

for nombre in nombres:

    resultat = str(int(nombre) * 5)

    equation = f"5 x {nombre} = {resultat}"

    resultats.append(equation)
#------------------------------------------3---------------------------------------------------

i = 1


while True:

    resultat = i * 5

    print(f"5 x {i} = {resultat}")

    i += 1

    if i > 10:b 
        break
#------------------------------------------4---------------------------------------------------


donnees = {"a": 42, "b": 42, "c": 42, "d": 42}


accumulateur = 42


for cle in donnees.keys():

    if cle == 'd':

        accumulateur -= 42
    else:

        accumulateur *= donnees[cle]


resultat = str(accumulateur)


print(resultat)
#------------------------------------------5---------------------------------------------------


nombre_lignes = 5
 
for i in range(1, nombre_lignes + 1):
    for j in range(i):
        print("*", end="")
    print(" ", end="")
#------------------------------------------6---------------------------------------------------


nbr = [5, 4, 3, 2, 1]


n = len(nbr)


for i in range(n):

    for j in range(0, n-i-1):

        if nbr[j] > nbr[j+1]:

            nbr[j], nbr[j+1] = nbr[j+1], nbr[j]


print(nbr)
#------------------------------------------7---------------------------------------------------

import datetime


annee_actuelle = datetime.datetime.now().year


annees = list(range(1980, annee_actuelle + 1))


print(annees)
#------------------------------------------8---------------------------------------------------


nombre_lignes = 8

for i in range(1, nombre_lignes + 1):
    for j in range(i):
        print("1", end="")
    print()
        
#-------------------------------------------9--------------------------------------------------

for i in range(10):
    espace1 = " " * (10 - i)
    crochet1 = "[" * i
    espace2 = " " * (10 - i)
    crochet2 = "]" * i
    print(espace1 + crochet1 + " " + crochet2 + espace2)
