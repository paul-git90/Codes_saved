# Afișează primele patru numere pare și restul numerelor impare până la 21
# Inițializăm un contor pentru numerele pare
contor_pare = 0

# Iterăm prin numerele de la 1 la 20
for numar in range(1, 21):
    if contor_pare < 4:
        # Verificăm dacă numărul este par
        if numar % 2 == 0:
            print(numar)
            contor_pare += 1
    else:
        # După primele 4 numere pare, afișăm numerele impare
        if numar % 2 != 0:
            print(numar)