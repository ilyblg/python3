#__________________________________rechercher fontion
def searchBook(bibliotheque):
    search = open(bibliotheque, 'r')
    f = search.readline()
    w=input("Saisir votre recherche : ")
    res = False
    nb=0
    liste=[]
    for f in search :
        if w in f :
            res = True
            print(f)
            nb=nb+1
    print("Votre recherche comporte ",nb,"résultats avec le mot '",w,"' :\n")
    if res == False :
        print("Aucun résultat.\n")
    search.close()
    return

#_____________________________________ajouter fontion
def addBook(bibliotheque):
    newBook=["e titre", "'auteur", "'éditeur", "'année", "'ISBN"]
    k=0
    while k<5 :
        n=input("Saisir l" + newBook[k] + " du livre : ")
        newBook[k]=n
        k=k+1
    else :
        v=input("Etes-vous sur d'entrer cet ouvrage ? oui/non ")
        if v=="oui" :
            fichier = open(bibliotheque,'a')
            fichier.write(str(newBook)+"\n")
            fichier.close()
            print(newBook[0]+" de "+newBook[1]+", ("+newBook[2]+", "+newBook[3]+"), "+" ISBN: "+newBook[4]+" a été ajouté avec succès.")
        elif v=="non" :
            q=input("Voulez-vous entrer un ouvrage à nouveau ? oui/non ")
            if q==oui :
                addBook(bibliotheque)
            elif q=="non" :
                return
        else :
            print("Votre choix n'est ni un 'oui' ni un 'non'. Veuillez recommencer s'il vous plaît.")
    return
#__________________________________supprimer_fonction
def delete(bibliotheque):
    d=input("Saisir un élément du livre à SUPPRIMER : ")
    with open(bibliotheque, 'r') as source, open(trash, 'w') as target:
        for l in source :
            if not d in l :
                target.write(l)
        source.close()
        target.close()
    with open(trash, 'r') as source, open(bibliotheque, 'w') as target:
        for l in source :
            target.write(l)
        source.close()
        target.close()
    return
#____________________________________afficher_fontion
def allBook(bibliotheque):
    show = open(bibliotheque, 'r')
    f = show.read()
    print("Voici la liste des ouvrages : ")
    print(f)
    show.close()
    return
#________________________MAIN________________________
bibliotheque = 'bibliotheque.txt'
trash = 'trash.txt'

print("0. Terminer")
print("1. Rechercher un ouvrage")
print("2. Ajouter un ouvrage")
print("3. Supprimer un ouvrage")
print("4. Afficher tous les ouvrages")

choix=int(input("Que voulez vous faire ?"))

while (choix < 5):
    if choix==1:
        searchBook(bibliotheque)
    elif (choix == 0):
        import sys
        sys.exit()     
    elif choix==2:
        addBook(bibliotheque)
    elif choix==3:
        delete(bibliotheque)
    elif choix==4:
        allBook(bibliotheque)
    else :
        print("Votre choix n'est pas disponible. Essayez encore.")
    print("0. Terminer")
    print("1. Rechercher un ouvrage")
    print("2. Ajouter un ouvrage")
    print("3. Supprimer un ouvrage")
    print("4. Afficher tous les ouvrages")
    choix=int(input("\nQue voulez vous faire ?\n"))
