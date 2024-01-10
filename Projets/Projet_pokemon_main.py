from Projet_pokemon_class import Pokemon
import random as r

card1=Pokemon('Bulbasaur',45,49,65,'Plante')
card2=Pokemon('Ivysaur',60,62,80,'Plante')
card3=Pokemon('Venusaur',80,82,100,'Plante')
card4=Pokemon('Charmander',39,52,60,'Feu')
card5=Pokemon('Charmeleon',58,64,80,'Feu')
card6=Pokemon('Charizard',78,84,109,'Feu') 
card7=Pokemon('Squirtle',44,48,50,'Eau')
card8=Pokemon('Wartortle',59,63,65,'Eau')
card9=Pokemon('Blastoise',79,83,85,'Eau')
card10=Pokemon('Caterpie',45,30,20,'Insecte')
card11=Pokemon('Metapod',50,20,25,'Insecte')
card12=Pokemon('Butterfree',60,45,90,'Insecte')
card13=Pokemon('Weedle',40,35,20,'Insecte')
card14=Pokemon('Kakuna',45,25,25,'Insecte')
card15=Pokemon('Beedrill',65,90,45,'Insecte')

jeu=[card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15]
r.shuffle(jeu)
player1=[]
player2=[]
for i in range(5):
    a=jeu.pop(0)
    b=jeu.pop(0)
    player1.append(a)
    player2.append(b) 

print("################################################################################################################################\n Deck joueur 1:")
for i in player1:
    print(i)
print("################################################################################################################################\n Deck joueur 2:")
for i in player2:
    print(i)

u=r.randint(1,2)
if u==1:
    print("Le joueur 1 commence à attaquer")
else:
    print("Le joueur 2 commence à attaquer")

def choix_card(choix_possibles,player):
    while True:
        print(player)
        choix = input("Quelle carte veux-tu utiliser?: ")
        if choix in choix_possibles:
            return choix
        else:
            print("Le pokémon entré est KO ou inexistant. Veuillez choisir parmi :",choix_possibles)

def choix_attaque(choix_possibles,player):
    while True:
        print(player)
        choix = input("Que souhaite tu faire? Lancer une <<Attaque normale>> ou une <<Attaque spéciale>>? (Attention tu ne peux utiliser une A spéciale qu'une seule fois dans toute la partie):   ")
        if choix in choix_possibles:
            return choix
        else:
            print("L'attaque selectionné n'existe pas ou a atteint son nombre d'utilisation maximun.\n Veuillez choisir parmi :",choix_possibles)


noms_attaque1=["Attaque spéciale","Attaque normale"]
noms_attaque2=["Attaque spéciale","Attaque normale"]
noms_pokemon1=[]
noms_pokemon2=[]

while len(player1) > 0 and len(player2) > 0:
    if u==1:
        for i in range(len(player1)):
            nom1=player1[i].get_nom()
            noms_pokemon1.append(nom1)
        choix_carte1=choix_card(noms_pokemon1,"Joueur 1")
        noms_pokemon1=[]
        for i in range(len(player1)):
            if choix_carte1==player1[i].get_nom():
                c1=player1[i]
        for i in range(len(player2)):
            nom2=player2[i].get_nom()
            noms_pokemon2.append(nom2)
        choix_carte2=choix_card(noms_pokemon2,"Joueur 2")
        noms_pokemon2=[]
        for i in range(len(player2)):
            if choix_carte2==player2[i].get_nom():
                c2=player2[i]
        choix_attaque1=choix_attaque(noms_attaque1,"Joueur 1")
        if choix_attaque1=='Attaque normale':
            l1=c2.attack(c1.get_attack())
            c2.set_HP(l1)
            pok_ko=c2.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player2.index(c2)
                player2.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
        elif choix_attaque1=='Attaque spéciale':
            noms_attaque1.remove("Attaque spéciale")
            l1=c2.special(c1.get_spe())
            c2.set_HP(l1)
            pok_ko=c2.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player2.index(c2)
                player2.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
        for i in range(len(player1)):
            nom1=player1[i].get_nom()
            noms_pokemon1.append(nom1)
        choix_carte1=choix_card(noms_pokemon1,"Joueur 1")
        noms_pokemon1=[]
        for i in range(len(player1)):
            if choix_carte1==player1[i].get_nom():
                c1=player1[i]
        for i in range(len(player2)):
            nom2=player2[i].get_nom()
            noms_pokemon2.append(nom2)
        choix_carte2=choix_card(noms_pokemon2,"Joueur 2")
        noms_pokemon2=[]
        for i in range(len(player2)):
            if choix_carte2==player2[i].get_nom():
                c2=player2[i]
        choix_attaque2=choix_attaque(noms_attaque2,"Joueur 2")
        if choix_attaque2=='Attaque normale':
            l2=c1.attack(c2.get_attack())
            c1.set_HP(l2)
            pok_ko=c1.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player1.index(c1)
                player1.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
        elif choix_attaque2=='Attaque spéciale':
            noms_attaque2.remove("Attaque spéciale")
            l2=c1.special(c2.get_spe())
            c1.set_HP(l2)
            pok_ko=c1.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player1.index(c1)
                player1.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
    else:
        for i in range(len(player1)):
            nom1=player1[i].get_nom()
            noms_pokemon1.append(nom1)
        choix_carte1=choix_card(noms_pokemon1,"Joueur 1")
        noms_pokemon1=[]
        for i in range(len(player1)):
            if choix_carte1==player1[i].get_nom():
                c1=player1[i]
        for i in range(len(player2)):
            nom2=player2[i].get_nom()
            noms_pokemon2.append(nom2)
        choix_carte2=choix_card(noms_pokemon2,"Joueur 2")
        noms_pokemon2=[]
        for i in range(len(player2)):
            if choix_carte2==player2[i].get_nom():
                c2=player2[i]
        choix_attaque2=choix_attaque(noms_attaque2,"Joueur 2")
        if choix_attaque2=='Attaque normale':
            l2=c1.attack(c2.get_attack())
            c1.set_HP(l2)
            pok_ko=c1.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player1.index(c1)
                player1.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
        elif choix_attaque2=='Attaque spéciale':
            noms_attaque2.remove("Attaque spéciale")
            l2=c1.special(c2.get_spe())
            c1.set_HP(l2)
            pok_ko=c1.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player1.index(c1)
                player1.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
        for i in range(len(player1)):
            nom1=player1[i].get_nom()
            noms_pokemon1.append(nom1)
        choix_carte1=choix_card(noms_pokemon1,"Joueur 1")
        noms_pokemon1=[]
        for i in range(len(player1)):
            if choix_carte1==player1[i].get_nom():
                c1=player1[i]
        for i in range(len(player2)):
            nom2=player2[i].get_nom()
            noms_pokemon2.append(nom2)
        choix_carte2=choix_card(noms_pokemon2,"Joueur 2")
        noms_pokemon2=[]
        for i in range(len(player2)):
            if choix_carte2==player2[i].get_nom():
                c2=player2[i]
        choix_attaque1=choix_attaque(noms_attaque1,"Joueur 1")
        if choix_attaque1=='Attaque normale':
            l1=c2.attack(c1.get_attack())
            c2.set_HP(l1)
            pok_ko=c2.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player2.index(c2)
                player2.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)
        elif choix_attaque1=='Attaque spéciale':
            noms_attaque1.remove("Attaque spéciale")
            l1=c2.special(c1.get_spe())
            c2.set_HP(l1)
            pok_ko=c2.KO()
            if pok_ko is not None: 
                print(pok_ko)
                index_pok_ko = player2.index(c2)
                player2.pop(index_pok_ko)
            print("################################################################################################################################\n Deck joueur 1:")
            for i in player1:
                print(i)
            print("################################################################################################################################\n Deck joueur 2:")
            for i in player2:
                print(i)

if len(player1)>len(player2):
    print("Le joueur 1 a gagné!!")
else:
    print("Le joueur 2 a gangé!!")


       