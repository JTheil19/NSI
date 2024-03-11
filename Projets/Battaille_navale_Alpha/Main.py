from Bib_main import *

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

affichage(jeu)
for i in range(2):
    placement_bateau(jeu)
affichage(jeu)

"""while jeu_stop(jeu)!=False:
     entry_attack=input("Attaque?: ").upper()
     liste_attaque=get_char(entry_attack)
     index_attaque_y=attack_y(liste_attaque)
     index_attaque_x=attack_x(liste_attaque)
     jeu_fonctionnement(index_attaque_y,index_attaque_x,jeu)
     affichage(jeu)"""