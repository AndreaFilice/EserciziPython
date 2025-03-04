#Esercizio 1

vetCitta = ["Milano", "Roma", "Napoli", "Vittuone"]
vetTMax = [28, 31, 34, 25]
vetTMin = [18, 21, 24, 17]

mediaMin = 0
mediaMax = 0

for i in range(len(vetTMin)):
    mediaMin += vetTMin[i]

for i in range(len(vetTMax)):
    mediaMax += vetTMax[i]

#PUNTO 1 E 2
print(f"Media temperature minime: {mediaMin/len(vetCitta)}")
print(f"Media temperature massime: {mediaMax/len(vetCitta)}")

#PUNTO 3
for i in range(len(vetTMin)):
        print(f"La città {vetCitta[i]} ha la temperatura minima sotto la media!")

#PUNTO 4
s = input("Inserisci un nome di una città: ")

if(s in vetCitta):
    print(f"La città {s} è presente!")
else:
    print(f"La città {s} non è presente")

#PUNTO 5
max = 0
min = 0

for i in range(len(vetCitta)):
    if(vetTMax[i] > vetTMax[max]):
        max = i
    if(vetTMin[i] < vetTMin[min]):
        min = i

print(f"La città con la temperatura più alta è: {vetCitta[max]}")
print(f"La città con la temperatura più bassa è: {vetCitta[min]}")


#Esercizio 2
oreP = []
oreA = []
destinazioni = []

#INSERISCI DATI INPUT

dimensione = int(input("Inserisci quante corse vuoi memorizzare: "))

for i in range(dimensione):
    destinazione = input("Inserisci la destinazione: ")
    oraP = int(input("Inserisci l'orario di partenza: "))
    oraA = int(input("Inserisci l'orario di arrivo: "))
    destinazioni.append(destinazione)
    oreP.append(oraP)
    oreA.append(oraA)

#INSERIMENTO DESTINAZIONE
print("\n------CONFRONTA ORARI-------\n")

s = input("Inserisci la destinazione per visualizzare l'orari: ")

#CONTROLLO DESTINAZIONE
while (s not in destinazioni):
    s = input("Inserisci una destinazione corretta per visualizzare gli orari: ")

#TROVA DESTINAZIONE
for i in range(dimensione):
    if(s == destinazioni[i]):
        print(f"ORARIO DI PARTENZA PREVISTO PER {s}: {oreP[i]}, ORARIO DI ARRIVO PREVISTO PER {s}: {oreA[i]}")

#ORARIO DI TEMPO

print("\n------TROVA ORARIO IN RANGE-------\n")
valoreMin = int(input("Inserisci l'orario di partenza minimo: "))
valoreMax = int(input("Inserisci l'orario di partenza massimo: "))

for i in range(dimensione):
    if(oreP[i] >= valoreMin and oreP[i] <= valoreMax):
        print(f"TROVATA PARTENZA PER {destinazioni[i]} ALLE {oreP[i]}")

#CONFRONTA MINOR TEMPO

print("\n------TROVA CORSA PIU' VELOCE-------\n")

tempoS = input("Inserisci la destinazione per confrontare il tempo di percorso: ")

while (s not in destinazioni):
    tempoS = input("Inserisci una destinazione corretta per visualizzare il tempo di percorso: ")

durataMinore = 100
indexDurata = 0

for i in range(dimensione):
    if(tempoS == destinazioni[i]):
        durata = oreA[i] - oreP[i]
        if(durata < durataMinore):
            durataMinore = durata
            indexDurata = i

for i in range(dimensione):
    if((oreA[i] - oreP[i]) == durataMinore):
        print(f"PARTENZA PER {tempoS} DI MINOR DURATA, PARTENZA ALLE ORE: {oreP[i]} DURATA: {(oreA[i] - oreP[i])} ORE.")