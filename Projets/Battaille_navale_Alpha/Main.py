from Bib_main import *
import random as randint

jeu=[[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]]

jeu_ordi=[[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]]

affichage(jeu)
for i in range(3):
     placement_bateau(jeu)
     affichage(jeu)

for i in range(3):
     placement_bateau_auto(jeu_ordi)

while jeu_stop(jeu_ordi) and jeu_stop(jeu)!=False:
     entry_attack=input("Attaque?: ").upper()
     liste_attaque=get_char(entry_attack)
     index_attaque_y=attack_y(liste_attaque)
     index_attaque_y_ordi=randint.randint(0,9)
     index_attaque_x=attack_x(liste_attaque)
     index_attaque_x_ordi=randint.randint(0,9)
     jeu_fonctionnement(index_attaque_y,index_attaque_x,jeu_ordi)
     print("Attaques réalisées: \n")
     affichage(jeu_ordi)
     jeu_fonctionnement(index_attaque_y_ordi,index_attaque_x_ordi,jeu)
     print("Attaques subites: \n")
     affichage(jeu)