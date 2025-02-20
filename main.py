# PROGETTO CARTA FORBICE SASSO
from funzioni_utili import scelta_mossa
from funzioni_utili import gioco
from pprint import pprint

diz = {
        "Vittorie" : 0,
        "Sconfitte" : 0,
        "Pareggi" : 0
    }

nickname = input("Inserisci il tuo nickname: ")

while True:
    risultato = gioco()
    print(risultato)

    if "vinto" in risultato:
        diz["Vittorie"] += 1

    elif "perso" in risultato:
        diz["Sconfitte"] += 1

    else:
        diz["Pareggi"] += 1

    richiesta = input("\nVuoi giocare ancora? Sì o No? ")

    if richiesta == "Sì":
        continue
        # ris = gioco()
        # print(ris)

    elif richiesta == "No":
        print(f" ----- Registro partite di {nickname} -----")
        pprint(diz)
        break

    else:
        while richiesta != "Sì" or richiesta != "No":
            print("Scelta non valida! Scegliere: Sì o No")