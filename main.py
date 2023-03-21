def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne +", quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR : Veuillez entrer un age correct")
    return age_int

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom

def demander_mdp():
    mdp = ""

    while not mdp == "Zeraxpsy":
        mdp = input("Veuillez entrer votre mots de passe ! ")

    print("Mots de passe correct !")
    return mdp

def afficher_information_personnel(nom,age):
    print()
    print("Vous vous appellez " + nom + ", vous avez " + str(age) + "ans et l'an prochain vous aurez " + str(age + 1) + "ans !")
    if age == 17:
        print("Vous etes presque majeur ! ")
    elif age == 18:
        print("Vous etes tout juste majeur : felicitation !! ")
    elif age <= 10:
        print("Vous etes un enfant .")
    elif age >= 60:
        print("Vous etes un senior !")
    elif age <= 18:
        print("Vous etes mineur . ")
    else:
        print("Vous etes majeur . ")

nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

afficher_information_personnel(nom1, age1)
afficher_information_personnel(nom2, age2)
