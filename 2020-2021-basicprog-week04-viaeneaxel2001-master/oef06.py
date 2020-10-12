woord = input("Geef een woord op? > ")

klinkers = []
medeklinkers = []

for letter in woord.lower():
    if letter == "a" or letter =="e" or letter =="u" or letter =="o" or letter =="i":
        klinkers.append(letter)
    else:
        medeklinkers.append(letter)


print(f"De klinkers zijn {klinkers}")
print(f"De medeklinkers zijn {medeklinkers}")

