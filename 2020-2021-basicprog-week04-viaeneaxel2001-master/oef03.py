vrienden = []

naam = input("Geef de naam van een vriend op, of sluit af met een leeg veld: > ")

while naam != "":
   # naam opslaan in list
   vrienden.append(naam)
   # opnieuw de vraag stellen
   naam = input(
       "Geef de naam van een vriend op, of sluit af met een leeg veld: >")

print(f"{vrienden}")