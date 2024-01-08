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


if u==1:
    choix_carte1=str(input("Joueur 1:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player1)):
        if choix_carte1==player1[i].get_nom():
            c1=player1[i]
    choix_carte2=str(input("Joueur 2:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player2)):
        if choix_carte2==player2[i].get_nom():
            c2=player2[i]
    choix_attaque1=str(input("Joueur 1:\n Que souhaite tu faire? Lancer une attaque normale ou une attaque spéciale? (Attention tu ne peux utiliser une attaque spéciale qu'une seule fois dans toute la partie): "))
    if choix_attaque1=='attaque normale':
       l1=c2.attack(c1.get_attack())
       c2.set_HP(l1)
       c2.KO()
       if c2.KO()==True:
            player2.pop(c2)
       print("################################################################################################################################\n Deck joueur 1:")
       for i in player1:
            print(i)
       print("################################################################################################################################\n Deck joueur 2:")
       for i in player2:
            print(i)
    elif choix_attaque1=='attaque spéciale':
        l1=c2.special(c1.get_spe())
        c2.set_HP(l1)
        c2.KO()
        if c2.KO()==True:
            player2.pop(c2)
        print("################################################################################################################################\n Deck joueur 1:")
        for i in player1:
            print(i)
        print("################################################################################################################################\n Deck joueur 2:")
        for i in player2:
            print(i)
    choix_carte1=str(input("Joueur 1:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player1)):
        if choix_carte1==player1[i].get_nom():
            c1=player1[i]
    choix_carte2=str(input("Joueur 2:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player2)):
        if choix_carte2==player2[i].get_nom():
            c2=player2[i]
    choix_attaque2=str(input("Joueur 2:\nQue souhaite tu faire? Lancer une attaque normale ou une attaque spéciale? (Attention tu ne peux utiliser une attaque spéciale qu'une seule fois dans toute la partie): "))
    if choix_attaque2=='attaque normale':
       l2=c1.attack(c2.get_attack())
       c1.set_HP(l2)
       c1.KO()
       if c1.KO()==True:
            player1.pop(c1)
       print("################################################################################################################################\n Deck joueur 1:")
       for i in player1:
            print(i)
       print("################################################################################################################################\n Deck joueur 2:")
       for i in player2:
            print(i)
    elif choix_attaque2=='attaque spéciale':
        l2=c1.special(c2.get_spe())
        c1.set_HP(l2)
        c1.KO()
        if c1.KO()==True:
            player1.pop(c1)
        print("################################################################################################################################\n Deck joueur 1:")
        for i in player1:
            print(i)
        print("################################################################################################################################\n Deck joueur 2:")
        for i in player2:
            print(i)
else:
    choix_carte1=str(input("Joueur 1:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player1)):
        if choix_carte1==player1[i].get_nom():
            c1=player1[i]
    choix_carte2=str(input("Joueur 2:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player2)):
        if choix_carte2==player2[i].get_nom():
            c2=player2[i]
    choix_attaque2=str(input("Joueur 2:\nQue souhaite tu faire? Lancer une attaque normale ou une attaque spéciale? (Attention tu ne peux utiliser une attaque spéciale qu'une seule fois dans toute la partie): "))
    if choix_attaque2=='attaque normale':
       l2=c1.attack(c2.get_attack())
       c1.set_HP(l2)
       c1.KO()
       if c1.KO()==True:
            player1.pop(c1)
       print("################################################################################################################################\n Deck joueur 1:")
       for i in player1:
            print(i)
       print("################################################################################################################################\n Deck joueur 2:")
       for i in player2:
            print(i)
    elif choix_attaque2=='attaque spéciale':
        l2=c1.special(c2.get_spe())
        c1.set_HP(l2)
        c1.KO()
        if c1.KO()==True:
            player1.pop(c1)
        print("################################################################################################################################\n Deck joueur 1:")
        for i in player1:
            print(i)
        print("################################################################################################################################\n Deck joueur 2:")
        for i in player2:
            print(i)
    choix_carte1=str(input("Joueur 1:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player1)):
        if choix_carte1==player1[i].get_nom():
            c1=player1[i]
    choix_carte2=str(input("Joueur 2:\n Quelle carte veux-tu utiliser?: "))
    for i in range(len(player2)):
        if choix_carte2==player2[i].get_nom():
            c2=player2[i]
    choix_attaque1=str(input("Joueur 1:\n Que souhaite tu faire? Lancer une attaque normale ou une attaque spéciale? (Attention tu ne peux utiliser une attaque spéciale qu'une seule fois dans toute la partie): "))
    if choix_attaque1=='attaque normale':
       l1=c2.attack(c1.get_attack())
       c2.set_HP(l1)
       c2.KO()
       if c2.KO()==True:
            player2.pop(c2)
       print("################################################################################################################################\n Deck joueur 1:")
       for i in player1:
            print(i)
       print("################################################################################################################################\n Deck joueur 2:")
       for i in player2:
            print(i)
    elif choix_attaque1=='attaque spéciale':
        l1=c2.special(c1.get_spe())
        c2.set_HP(l1)
        c2.KO()
        if c2.KO()==True:
            player2.pop(c2)
        print("################################################################################################################################\n Deck joueur 1:")
        for i in player1:
            print(i)
        print("################################################################################################################################\n Deck joueur 2:")
        for i in player2:
            print(i)
#while deck_empty()!=True:
#    pass


       