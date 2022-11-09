import random
def pierreFeuilleCiseau(userName=None):

    iaCoup = ["pierre","feuille","ciseau"]
    ListeAction = []
    ListeScore = []
    
    if userName == None:
        userName = str(input("Qu'elle est ton pseudo ? :"))
    boCombien = int(input("En combien de victoire veut tu arreter ? (Bo1 : 1 / Bo2 : 2 / Bo3 : 3 ...) :"))
    
    print("Voici les coups que tu peut jouer : ")
    print("Pierre : P / Feuille : F / Ciseau : C")
    print("Pour jouer écris l'une de ces lettres afin de selectionner un coups")
    
    
    
    
    scoreJ = 0
    scoreIa = 0
    
    while scoreJ!=boCombien and scoreIa!=boCombien:
        
        print(' ')

        print("Pierre : P / Feuille : F / Ciseau : C")
        jAction = str(input("Qu'elle est ton coup " +userName+  " ? :"))
        iaAction = iaCoup[random.randrange(0,3)]

        if (jAction == "P" or jAction == "p") and iaAction == "pierre":
            print("Pierre contre Pierre !")
            print("Egalité !")
            ListeAction.append("Pierre : Pierre") 
        elif (jAction == "F" or jAction == "f") and iaAction == "feuille":
            print("Feuille contre Feuille !")
            print("Egalité !")
            ListeAction.append("Feuille : Feuille")
        elif (jAction == "C" or jAction == "c") and iaAction == "ciseau":
            print("Ciseau contre Ciseau !")
            print("Egalité !")
            ListeAction.append("Ciseau : Ciseau")
        
        elif (jAction == "P" or jAction == "p") and iaAction == "feuille":
            print("Pierre contre Feuille !")
            print("Perdu !")
            scoreIa = scoreIa + 1
            ListeAction.append("Pierre : Feuille") 
        elif (jAction == "F" or jAction == "f") and iaAction == "ciseau":
            print("Feuille contre ciseau !")
            print("Perdu !")
            scoreIa = scoreIa + 1
            ListeAction.append("Feuille : Ciseau")
        elif (jAction == "C" or jAction == "c") and iaAction == "pierre":
            print("Ciseau contre Pierre !")
            print("Perdu !")
            scoreIa = scoreIa + 1
            ListeAction.append("Ciseau : Pierre")

        elif (jAction == "P" or jAction == "p") and iaAction == "ciseau":
            print("Pierre contre Ciseau !")
            print("Gagné !")
            scoreJ = scoreJ + 1
            ListeAction.append("Pierre : Ciseau")
        elif (jAction == "F" or jAction == "f") and iaAction == "pierre":
            print("Feuille contre Pierre !")
            print("Gagné !")
            scoreJ = scoreJ + 1
            ListeAction.append("Feuille : Pierre")
        elif (jAction == "C" or jAction == "c") and iaAction == "feuille":
            print("Ciseau contre Feuille !")
            print("Gagné !")
            scoreJ = scoreJ + 1
            ListeAction.append("Ciseau : Feuille")
        
        ListeScore.append(str(scoreJ) +" : "+str(scoreIa))

    print(' ')
    print("La partie est finis !")
    if scoreJ > scoreJ:
        print("Vous avez gagné "+userName)
    else:
        print("L'IA à gagnée !")
    print(' ')
    print("Récapitulatif de la partie :")
    for i in range(len(ListeAction)):
        print(ListeScore[i])
        print(ListeAction[i])
    
    restart = str(input("Voulez vous rejouer ? (oui , non) : "))
    if restart != "oui" and restart !="non":
        print("désolé je n'ai pas compris")
        restart = str(input("Voulez vous rejouer ? (oui , non) : "))
    if restart == "oui":
        pierreFeuilleCiseau(userName)

pierreFeuilleCiseau()