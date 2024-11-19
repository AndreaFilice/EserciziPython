#EESERCIZIO 1

voto1 = int(input("Inserisci il primo voto in trentesimi: "))
while(voto1 < 18 or voto1 > 30):
    voto1 = int(input("Inserisci il primo voto IN TRENTESIMI (da 18 a 30): "))

voto2 = int(input("Inserisci il secondo voto in trentesimi: "))
while(voto2 < 18 or voto2 > 30):
    voto2 = int(input("Inserisci il primo voto IN TRENTESIMI (da 18 a 30): "))

voto3 = int(input("Inserisci il terzo voto in trentesimi: "))
while(voto3 < 18 or voto3 > 30):
    voto3 = int(input("Inserisci il primo voto IN TRENTESIMI (da 18 a 30): "))

tipoDiMedia = int(input("La media si vuole calcolata in CENTESIMI (1) oppure in TRENTESIMI(2)?"))

while(tipoDiMedia != 1 and tipoDiMedia != 2):
    tipoDiMedia = int(input("Tipo di media errata, re-inserisci se CENTESIMI (1) o TRENTESIMI (2)"))

if(tipoDiMedia == 1):
    mediaTotale = int((voto1 + voto2 + voto3) * (100/30) / 3)
    print(f"La media totale in CENTESIMI è: {mediaTotale}")

else:
    mediaTotale = int((voto1 + voto2 + voto3) /3)
    print(f"La media totale in TRENTESIMI è: {mediaTotale}")


#ESERCIZIO 2

mediaAlunno = int(input("Inserisci la tua media: ")) 
classeAlunno = int(input("Insersci l'anno scolastico "))

if(classeAlunno < 3 and classeAlunno > 5):
    print("Classe errata!")

if(classeAlunno == 3):
    if(mediaAlunno == 6):
        print("Il credito dell'alunno è di 7-8")
    elif(mediaAlunno > 6 and mediaAlunno <= 7):
        print("Il credito dell'alunno è di 8-9")
    elif(mediaAlunno > 7 and mediaAlunno <= 8):
        print("Il credito dell'alunno è di 9-10")
    elif(mediaAlunno > 8 and mediaAlunno <= 9):
        print("Il credito dell'alunno è di 10-11")
    elif(mediaAlunno > 9 and mediaAlunno <=10):
        print("Il credito dell'alunno è di 11-12")
    else:
        print("Media errata!")
    
if(classeAlunno == 4):
    if(mediaAlunno == 6):
        print("Il credito dell'alunno è di 8-9")
    elif(mediaAlunno > 6 and mediaAlunno <= 7):
        print("Il credito dell'alunno è di 9-10")
    elif(mediaAlunno > 7 and mediaAlunno <= 8):
        print("Il credito dell'alunno è di 10-11")
    elif(mediaAlunno > 8 and mediaAlunno <= 9):
        print("Il credito dell'alunno è di 11-12")
    elif(mediaAlunno > 9 and mediaAlunno <=10):
        print("Il credito dell'alunno è di 12-13")
    else:
        print("Media errata!")

if(classeAlunno == 5):
    if(mediaAlunno == 6):
        print("Il credito dell'alunno è di 9-10")
    elif(mediaAlunno > 6 and mediaAlunno <= 7):
        print("Il credito dell'alunno è di 10-11")
    elif(mediaAlunno > 7 and mediaAlunno <= 8):
        print("Il credito dell'alunno è di 11-12")
    elif(mediaAlunno > 8 and mediaAlunno <= 9):
        print("Il credito dell'alunno è di 13-14")
    elif(mediaAlunno > 9 and mediaAlunno <=10):
        print("Il credito dell'alunno è di 14-15")
    else:
        print("Media errata!")

#ESERCIZIO 3
lanciTotali = 0
lancio1 = int(input("Inserisci la lunghezza del primo lancio: "))
if(lancio1 > 0):
    lanciTotali += 1

lancio2 = int(input("Inserisci la lunghezza del secondo lancio: "))
if(lancio2 > 0):
    lanciTotali += 1

lancio3 = int(input("Inserisci la lunghezza del terzo lancio: "))
if(lancio3 > 0):
    lanciTotali += 1

lancio4 = int(input("Inserisci la lunghezza del quarto lancio: "))
if(lancio4 > 0):
    lanciTotali += 1

lancio5 = int(input("Inserisci la lunghezza del quinto lancio: "))
if(lancio5 > 0):
    lanciTotali += 1

mediaTotale = (lancio1 + lancio2 + lancio3 + lancio4 + lancio5) / lanciTotali

print(f"Lanci totali: {lanciTotali}")
print(f"La media dei lanci è: {mediaTotale}")