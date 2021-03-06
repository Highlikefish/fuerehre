# KronenkorkenPyramide
# Regeln: Pro Reihe -> N + 1, N = Anzahl Kronenkorken (Reihe 1, N = 1)
# Ziel: Input -> Anzahl Reihen, Output -> benötigte Kronenkorken

i = 1

while i == 1:
    try:
        # Anzahl der Reihen r
        r = int(input("Anzahl gewünschter Reihen: "))
        # Rechnung Gaußsche Summenformel
        K = int((r * (r + 1)) / 2)
    # Eingabe überprüfen
    except ValueError:
        print("Das ist keine ganze Zahl, probiers nochmal.")
        continue
    else:
        # break while
        i = 0
else:
    print("Anzahl benötigter Kronenkorken:", K)
