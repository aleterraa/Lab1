# PROGETTO CARTA FORBICE SASSO
import csv
from funzioni_utili import scelta_mossa
from funzioni_utili import gioco
from pprint import pprint

with open("Punteggi.csv", mode = "w", encoding='utf-8') as file:
    file.write("nickname, tot_vittorie, tot_pareggi, tot_sconfitte")

diz = {
        "Vittorie" : 0,
        "Sconfitte" : 0,
        "Pareggi" : 0
    }
richiesta = "Sì"

while richiesta == "Sì":
    nickname = input("Inserisci il tuo nickname: ")
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
        with open("Punteggi.csv", mode="a", encoding='utf-8') as file:
            file.write(f"{nickname}, {diz["Vittorie"]}, {diz["Pareggi"]}, {diz["Sconfitte"]}")
        break


    else:
        print("Scelta non valida! Scegliere: Sì o No")
        richiesta = input("\nVuoi giocare ancora? Sì o No? ")

