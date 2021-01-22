#progamme interactif
#Marceline Tambwe, tammar28@ecolecatholique.ca
#2020-12-05


print("Qu'est ce qui contient du sucre et qui malgré tout n'est pas sucré")
print("   (tape une réponse et tape sur Enter)") # message d'aide
input() # on attend le Enter mais ne garde pas ce que l'utiliatuer inscrit
print("le sucrier") #afficher ça peu importe -> "le sucrier"
print()

print("Il faut pédaler pour me faire avancer. On peut monter sur ma selle. J'ai un gidon et deux roues") 
print("   (taper une reponse et tape sur Entrer)") # message d'aide
input() # on attend le Enter mais ne garder pas ce que l'utuliatuer inscrit
print("le velo") #afficher ca peu importe -> "Le velo"
print()

print("pourquoi le poulet at-il traversé la route")
print("   (taper une reponse et tape sur Entrer)") # message d'aide
input() # on attend le Enter mais ne garder pas ce que l'utuliatuer inscrit
print("pour aller de l'autre cote") #afficher ca peu importe -> "pour aller de l'autre cote"
print()

print("Combien de pays y a t'il en Afrique")
# afficher ces choix :
print ("54")
print ("90")
print ("63")
print ("33")
print("   (tape une réponse et tape sur Enter)") # message d'aide
# attendre et garder la réponse -> input()
reponse = input()
# vérifier la réponse : if, elif, else (conditions)
if reponse == "54":
    print("faux. la bonne réponse est 63!")
elif reponse == "90":
    print("faux. la bonne réponse est 63!")
elif reponse == "63":
    print("vrai! bravo!!!")
elif reponse == "33":
    print("faux. la bonne réponse est 63!")
else:
    print(reponse, "n'était pas un choix valide")

# afficher la question
print("quel langue est la plus parler au monnde")
# afficher ces choix :
print("a. Anglais")
print ("b. Mandarin")
print ("c. Francais")
print ("d. L'espagnol")
print("   (tape la lettre de la réponse et tape sur Enter)") # message d'aide

# attendre et garder la réponse -> input()
reponse = input()
# vérifier la réponse : if, elif, else (conditions)
if reponse == "Anglais":
    print("faux. la bonne réponse est Mandarin!")
elif reponse == "L'espagnole":
    print("faux. la bonne réponse est Mandarin!")
elif reponse ==  "Mandarin":
    print("vrai! bravo!!!")
elif reponse ==  "Francais":
    print("faux. la bonne réponse est Mandarin!")
else:
    print(reponse, "n'était pas un choix valide")

# ajouter une autre question
print ("Avez vous aimer")
print("   (taper une reponse et tape sur Entrer)") # message d'aide
input() # on attend le Enter mais ne garder pas ce que l'utuliatuer inscrit

#afficher -> "Merci!!! d'avoir jouer a la prochaine."