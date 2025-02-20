#Libreria di funzioni per giocare a carta, forbice e sasso
def scelta_mossa():
    print("Scegli: Carta (C), Forbice (F) o Sasso (S)")
    scelta = input("Scegli la mossa: ")
    return scelta

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

if __name__ == "__main__":
    print("Benvenuto nella risorsa 'funzioni_utili'. Questa risorsa include due funzioni: scelta_mossa() e gioco(scelta1, scelta2)")
    print("Ecco due demo di codice.")

    # Esempio di utilizzo della funzione scelta_mossa
    print("Demo: Scegli una mossa")
    scelta = scelta_mossa()
    print(f"La mossa che hai scelto è {scelta}")
    
    # Esempio di utilizzo della funzione gioco
    scelta1 = "C"
    scelta2 = "F"
    print(f"{scelta1= } {scelta2= }")
    gioco = gioco(scelta1, scelta2)
