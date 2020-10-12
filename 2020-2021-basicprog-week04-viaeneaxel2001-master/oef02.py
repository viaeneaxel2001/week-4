nieuwe_list_getallen = []

for getal in range(1,483, 13):
    nieuwe_list_getallen.append(getal)
# print(f"{nieuwe_list_getallen}")

nieuwe_list_getallen.reverse()
# print(f"{nieuwe_list_getallen}")

del nieuwe_list_getallen[0]
nieuwe_list_getallen.remove(365)
print(f"{nieuwe_list_getallen}")