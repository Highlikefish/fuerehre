# KronenkorkenPyramide
# Regeln: Pro Reihe -> N + 1, N = Anzahl Kronenkorken (Reihe 1, N = 1)
# Ziel: Input -> Anzahl Reihen, Output -> benötigte Kronenkorken

i = 1

while i == 1:
    # Anzahl der Reihen r
    r = int(input("Anzahl gewünschter Reihen: "))
    # Rechnung Gaußsche Summenformel
    K = (r * (r + 1)) / 2
    # break while
    i = 0
else:
    print("Anzahl benötigter Kronenkorken:", K)
