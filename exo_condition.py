import random
from datetime import datetime
#---------------------1--------------------------------------

age = int(input("Entrez votre âge : "))

if age >= 18 and age < 42:
    print("Vous pouvez entrer, vous êtes majeur, vous avez", age, "ans.")
elif age >= 42:
    print("Vous êtes maintenant le patron de la boîte de nuit.")
else:
    print("Vous ne pouvez pas entrer, vous n'êtes pas majeur, vous avez", age, "ans.")
    
#--------------------------2----------------------------------------------------------

rand = random.randint(0, 30)

if rand >= 0 and rand <= 10:
    print("Cool")
elif rand >= 11 and rand <= 20:
    print("Tepid")
elif rand >= 21 and rand <= 30:
    print("Warm")
    
    
    

#--------------------------3----------------------------------------------------------

aujourd_hui = datetime.now()

jour = aujourd_hui.strftime("%A")

match jour:
    case "Monday":
        print("Nous sommes lundi.")
    case "Tuesday":
        print("Nous sommes mardi.")
    case "Wednesday":
        print("Nous sommes mercredi.")
    case "Thursday":
        print("Nous sommes jeudi.")
    case "Friday":
        print("Nous sommes vendredi.")
    case "Saturday":
        print("Nous sommes samedi.")
    case "Sunday":
        print("Nous sommes dimanche.")
    case _:
        print("Erreur: jour non reconnu.")       
        
 #-------------------------------4----------------------------------------------------------       
        print("Bienvenue dans l'aventure $")

print("Vous vous retrouvez devant unepo rte ")

choix1 = input("Voulez-vous ouvrir la porte ? (oui/non): ")

if choix1.lower() == "oui":
    print("Vous poussez la porte et entrez ")
    
    choix2 = input("Vous trouvez deux passages, l'un à gauche et l'autre à droite. Lequel choisissez-vous ? (gauche/droite): ")

    if choix2.lower() == "gauche":
        print("Vous avez gagner!")
    elif choix2.lower() == "droite":
        print("Vous suivez le passage à droite ")
        print("Vous tombez dans un trou.")
    else:
        print("Mauvais choix perdu")

else:
    print("Vous décidez de ne pas ouvrir la porte et de retourner chez vous.")

print("Merci d'avoir joué ! La grande réponse sur la vie, l'univers et le reste !")

#------------------------------------------5---------------------------------------------------------------

resultat = "42" if "ma_variable" in locals() or "ma_variable" in globals() else "cette variable n'existe pas"

#----------------------------------6-----------------------------------------------------------------------------------

prix_initial = float(input("Entrez le prix initial de l'article : "))

pourcentage_remise = float(input("Entrez le pourcentage de remise : "))

montant_remise = prix_initial * (pourcentage_remise / 100)

prix_final = prix_initial - montant_remise

if prix_final > prix_initial / 2:
    print("Montant de la remise :", montant_remise)
    print("Prix final après remise :", prix_final)
else:
    print("La remise est trop élevée. Le prix final est inférieur à la moitié du prix initial.")


#----------------------------------7----------------------------------------------------------------------------------

nombre_entree = input("Entrez un nombre entier : ")

if nombre_entree % 2 == 0:
    print("Le nombre", nombre_entree, "est pair.")
else:
    print("Le nombre", nombre_entree, "n'est pas pair.")