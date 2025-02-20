# PROGETTO CARTA FORBICE SASSO
from funzioni_utili import scelta_mossa
from funzioni_utili import gioco

while True:
    scelta1 = scelta_mossa()
    scelta2 = scelta_mossa()
    gioco(scelta1, scelta2)
    richiesta = input("Vuoi giocare ancora? Sì o No? ")
    if richiesta == "Sì":
        scelta1 = scelta_mossa()
        scelta2 = scelta_mossa()
        gioco(scelta1, scelta2)
    elif richiesta == "No":
        break
    else:
        print("Scelta non valida! Scegliere: Sì o No")


