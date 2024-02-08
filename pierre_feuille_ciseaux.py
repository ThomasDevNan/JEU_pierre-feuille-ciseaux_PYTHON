import random

#La liste des différents choix
choix=['P','F','C']

#Variables pour calculer les résultats qui seront incrémentées au fur et à mesures
score_cpu = 0
score_joueur = 0

#While permet de réexecuter le programme tant que nous voulons joueur
while True:
    # Randon d'un des choix
    cpu = random.choice(choix)

    # Saisie du joueur
    joueur = str(input('P: Pierre, F: Feuille, C: Ciseaux, Pour terminer, taper FIN')).capitalize()

    #Les 4 cas du jeu
    if joueur == cpu:
        print("égalité !")
    elif joueur == 'P':
        if cpu == 'F':
            print('Vous avez perdu, la feuille enveloppe la pierre')
            score_cpu+=1
        elif cpu == 'C':
            print('Vous gagnez, la pierre casse les ciseaux')
            score_joueur += 1
    elif joueur == 'F':
        if cpu == 'C':
            print('Vous avez perdu, les ciseaux coupent la feuille')
            score_cpu += 1
        elif cpu == 'P':
            print('Vous gagnez, la feuille enveloppe la pierre')
            score_joueur += 1
    elif joueur == 'C':
        if cpu == 'P':
            print('Vous avez perdu, la pierre casse les ciseaux')
            score_cpu += 1
        elif cpu == 'F':
            print('Vous gagnez, les ciseaux coupent la feuille')
            score_joueur += 1
    elif joueur == 'Fin':
        print('Résultats finaux : ')
        print(f'CPU : {score_cpu}')
        print(f'Joueur : {score_joueur}')
        if score_cpu == score_joueur:
            print('EGALITE !! Bravo à vous deux')
        elif score_cpu < score_joueur:
            print("L'homme bat la machine")
        else:
            print("La machine bat l'homme")
        break
    else:
        print("Je n'ai pas compris, vérifier l'orthographe")
