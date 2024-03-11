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

def placement_bateau(jeu):
     case=input("Ou voulez vous placer le bateau?(case):").upper()
     placement=get_char(case)
     position_x=attack_x(placement)
     position_y=attack_y(placement) 
     sens=input("Souhaites-tu placer ton navire verticalement ou horizontalement?(V ou H): ").upper()
     taille=int(input("Quelle taille est ton navire?(max:5): "))
#Si le bateau depasse du plateau
     if (sens == "H" and position_y + taille > len(jeu[0])) or \
       (sens == "V" and position_x + taille > len(jeu)):
        print("Erreur: Le bateau dépasse la zone de jeu. Veuillez réessayer.")
        return

#Si la place est deja rpsie
     for i in range(taille):
          if sens == "H" and jeu[position_x][position_y + i] == 1 or \
               sens == "V" and jeu[position_x + i][position_y] == 1:
               print("Erreur: La case est déjà occupée. Veuillez réessayer.")
               return
        
     if sens=="H":
          for i in range(taille):
               jeu[position_x][position_y+i]=1
     elif sens=="V":
          for i in range(taille):
               jeu[position_x+i][position_y]=1

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

def attack_y(pos):
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
     return index_y

def attack_x(pos):
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
     return index_x


def jeu_fonctionnement(index_y,index_x,jeu):
     if jeu[index_x][index_y]==0:
          jeu[index_x][index_y]=3
     elif jeu[index_x][index_y]==1:
          jeu[index_x][index_y]=2
     
     