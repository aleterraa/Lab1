from random import choice

#Libreria di funzioni per giocare a carta, forbice e sasso
def scelta_mossa():
    print("Scegli: Carta (C), Forbice (F) o Sasso (S)")
    scelta = input("Scegli la mossa: ")
    return scelta

def cpu():
    lista_mosse = ["C", "F", "S"]
    scelta = choice(lista_mosse)

    return scelta

def gioco():
    from funzioni_utili import scelta_mossa
    scelta_utente = scelta_mossa()
    scelta_cpu = cpu()
    diz = {
        "Vittorie": 0,
        "Sconfitte": 0,
        "Pareggi": 0
    }
    print(f"Il computer aveva scelto {scelta_cpu}")

    if scelta_utente == scelta_cpu:
        diz["Pareggi"] += 1
        return "Siete pari! Riscegliere le mosse"

    elif scelta_utente == "C":
        if scelta_cpu == "S":
            diz["Vittorie"] += 1
            return "Hai vinto! Carta batte sasso"

        if scelta_cpu == "F":
            diz["Sconfitte"] += 1
            return "Hai perso! Forbice batte carta"

    elif scelta_utente == "S":
        if scelta_cpu == "C":
            diz["Sconfitte"] += 1
            return "Hai perso! Carta batte sasso"

        if scelta_cpu == "F":
            diz["Vittorie"] += 1
            return "Hai vinto! Sasso batte forbice"

    elif scelta_utente == "F":
        if scelta_cpu == "S":
            diz["Sconfitte"] += 1
            return "Hai perso! Sasso batte forbice"

        if scelta_cpu == "C":
            diz["Vittorie"] += 1
            return "Hai vinto! Forbice batte carta"

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
    gioco = gioco()