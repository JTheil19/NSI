def affichage(jeu):
     print("  ", end="")
     for i in range(10):
          print(f" {chr(65+i)}", end="")#affichage des lettres
     print("\n" + "   " + "_ " * 10)  # Ligne de séparation
     for i, ligne in enumerate(jeu):#compte le nbm d'element
          print(f"{i+1}|", end=" ")  # Afficher l'indice de ligne
          for case in ligne:
               if case == 0:
                    print("~", end=" ")
               elif case == 1:
                    print("B", end=" ")
               elif case == 2:
                    print("X", end=" ")
               elif case == 3:
                    print("O", end=" ")
          print()  # Nouvelle ligne après chaque ligne du plateau

def bateau(jeu,ligne,colonne,taille):
     for i in range(taille):
          jeu[ligne][colonne+i]=1
     

def jeu_stop(jeu):
     for ligne in jeu:
          for case in ligne:
               if case==1:
                    return True
     return False
               
def get_char(mot):
     i=[]
     for lettre in mot:
          i.append(lettre)
     return i

def attack(jeu,pos)
     if pos[0]=='A':
          index_y=0
     elif pos[0]=='B':
          index_y=1
     elif pos[0]=='C':
          index_y=2
     elif pos[0]=='D':
          index_y=3
     elif pos[0]=='E':
          index_y=4
     elif pos[0]=='F':
          index_y=5
     elif pos[0]=='G':
          index_y=6
     elif pos[0]=='H':
          index_y=7
     elif pos[0]=='I':
          index_y=8
     elif pos[0]=='J':
          index_y=9
     if pos[1]=='1':
          index_x=0
     elif pos[1]=='2':
          index_x=1
     elif pos[1]=='3':
          index_x=2
     elif pos[1]=='4':
          index_x=3
     elif pos[1]=='5':
          index_x=4
     elif pos[1]=='6':
          index_x=5
     elif pos[1]=='7':
          index_x=6
     elif pos[1]=='8':
          index_x=7
     elif pos[1]=='9':
          index_x=8
     elif pos[1]=='10':
          index_x=9

          