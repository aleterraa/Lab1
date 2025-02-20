# PROGETTO CARTA FORBICE SASSO

    print("Scegli: Carta (C), Forbice (F) o Sasso (S)")
    scelta = input("Scegli la mossa: ")
    return scelta

scelta1 = scelta_mossa()
scelta2 = scelta_mossa()

def gioco(scelta1, scelta2):
    if scelta1 == scelta2:
        print("Siete pari! Riscegliere le mosse")
        scelta1 = scelta_mossa()
        scelta2 = scelta_mossa()
        gioco(scelta1, scelta2)
    elif scelta1 == "C":
        if scelta2 == "S":
            print("Carta batte sasso")
        if scelta2 == "F":
            print("Forbice batte carta")
    elif scelta1 == "S":
        if scelta2 == "C":
            print("Carta batte sasso")
        if scelta2 == "F":
            print("Forbice batte carta")
    elif scelta1 == "F":
        if scelta2 == "S":
            print("Sasso batte forbice")
        if scelta2 == "C":
            print("Forbice batte carta")

gioco(scelta1, scelta2)


