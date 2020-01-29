### BONJOUR WILLIAM, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

### TRÈS BON CODE, BIEN COMMENTÉ! BRAVO!
### ET IL FONCTIONNE... MAIS EN EMPLOYANT UNE TECHNIQUE PAS VRAIMENT RECOMMANDÉE...
### JE T'EXPLIQUE POURQUOI DANS LES COMMENTAIRES CI-DESSOUS:

# (c) William d'Avignon - 2020
# coding : utf-8
#Variables de base
n = 20000
l2 = list()
l3 = list()
# t = range(20000,30150) #t pour test
# print(n) #test

l2.append(n)
for x in l2: ### TA BOUCLE FAIT UNE BOUCLE DANS UNE LISTE ("l2") QUI NE CONTIENT QU'UN SEUL ÉLÉMENT AU DÉPART
    # n = n+1 #mal placé
    l2.append(n)
    # print("https://montrealcampus.ca?p=" + str(n))    #confirmation de la variable n ### PARFAIT: IL EST TRÈS BIEN DE FAIRE DES "PRINT" DE TEMPS EN TEMPS POUR VÉRIFIER CE QUE NOTRE CODE FAIT ET SI ON EST SUR LA BONNE VOIE!
    l3.append("https://montrealcampus.ca?p=" + str(n))
    n = n+1 ### ICI, TU AUGMENTES LA VALEUR DE "n" ET TU FAIS EN SORTE QUE LA BOUCLE VA FONCTIONNER UNE FOIS DE PLUS.
    ### ET UNE FOIS DE PLUS.
    ### ET UNE FOIS DE PLUS.
    ### C'EST CE QU'ON APPELLE UNE BOUCLE INFINIE ET ON ESSAIE D'ÉVITER ÇA COMME LA PESTE EN INFORMATIQUE.
    if int(n) == 30151: ### AHAH! TU AS PRIS DE L'AVANCE SUR LE PROCHAIN COURS.
        ### TON "IF" PERMET DE BRISER LA BOUCLE INFINIE AVEC UN "BREAK"
        ### MAIS IL EST PRÉFÉRABLE DE DONNER UNE TAILLE BIEN DÉFINIE À TA BOUCLE DÈS LE DÉPART.
        break
print(*l3, sep = "\n") ### WOAH! VOILÀ DES PARAMÈTRES DE "PRINT" QUE JE NE CONNAISSAIS PAS! MERCI!
### COMME DIRAIT NEIL DEGRASSE TYSON: "There’s no shame in admitting what you don’t know. The only shame is pretending you know all the answers."
print(l3)
print(len(l3))