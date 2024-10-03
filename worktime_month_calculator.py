from datetime import datetime, timedelta

"""
Acest worktime compenseaza orele de somn la minim 240 ore somn pe luna pentru tura 12/48
"""


# Funcție pentru a calcula detaliile intervalului de timp
def calculeaza_interval(data_start1, data_sfarsit1):
    # Convertim stringurile de date în obiecte datetime
    start_date = datetime.strptime(data_start1, "%d.%m.%Y")
    end_date = datetime.strptime(data_sfarsit1, "%d.%m.%Y")

    # Asigurăm că data de început este înainte de data de sfârșit
    if start_date > end_date:
        print("Data de început trebuie să fie înainte de data de sfârșit.")
        return

    # Calculăm numărul total de zile între cele două date
    numar_zile = (end_date - start_date).days + 1  # +1 pentru a include și ziua de sfârșit
    numar_saptamani = numar_zile // 7  # Numărul de săptămâni
    zile_luna = [0] * 7  # index 0: Luni, 1: Marti, 2: Miercuri, 3: Joi, 4: Vineri, 5: Sambata, 6: Duminica
    ore_total = numar_zile * 24  # Numărul total de ore în interval

    # Parcurgem fiecare zi din intervalul dat
    for single_date in (start_date + timedelta(n) for n in range(numar_zile)):
        # Incrementăm contorii pentru zilele săptămânii
        zile_luna[single_date.weekday()] += 1  # .weekday() returnează 0= Luni, 6= Duminica
    zile_de_weekend = zile_luna[5] + zile_luna[6]  # aici se calculeaza cumulul de zile din weekend

    # Algoritm ciclic pentru Serviciu de securitate
    # 12 ore muncă, 8 ore somn, 16 ore libere, 12 ore muncă, 8 ore somn, 16 ore libere, 8 ore somn, 16 ore libere
    algoritm = [12, 8, 16, 12, 8, 16, 8, 16]
    total_ore = ore_total  # Ore totale disponibile
    ore_munca1, ore_libere1, ore_somn1 = 0, 0, 0  # Resetăm orele pentru noul calcul

    # Calculăm câte cicluri se pot aplica în intervalul dat
    while total_ore > 0:
        for ore in algoritm:
            if total_ore >= ore:
                if ore == 12:  # 12 ore muncă
                    ore_munca1 += ore
                elif ore == 8:  # 8 ore de somn
                    ore_somn1 += ore
                else:  # 16 ore libere
                    ore_libere1 += ore
                total_ore -= ore  # Scădem orele folosite
            else:
                break  # Oprire dacă nu mai sunt suficiente ore

    # Verificăm dacă orele de somn sunt mai mici de 240 și compensăm din orele libere
    if ore_somn1 < 240:
        diferenta = 240 - ore_somn1
        if ore_libere1 >= diferenta:
            ore_libere1 -= diferenta
            ore_somn1 += diferenta

    # Calculăm orele libere totale
    total_libere1 = ore_libere1 + ore_somn1  # Total liber = ore libere + ore somn

    print("\nREZULTAT\n")
    print(f"Zile de Luni: {zile_luna[0]}\nZile de Marti: {zile_luna[1]}\nZile de Miercuri: {zile_luna[2]}\n"
          f"Zile de Joi: {zile_luna[3]}\nZile de Vineri: {zile_luna[4]}\nZile de Sambata: {zile_luna[5]}\n"
          f"Zile de Duminica: {zile_luna[6]}")
    print(f"In acest interval avem {zile_de_weekend} zile de weekend cumulate")

    # Afișăm rezultatele pentru Serviciu de securitate
    print("\nRezultatele pentru Serviciu de securitate (12/48h):")
    print(f"Numar de zile in interval: {numar_zile}")
    print(f"Numar de saptamani in interval: {numar_saptamani}")
    print(f"Numar de ore in interval: {ore_total}")
    print(f"Ore muncite: {ore_munca1}\nOre libere: {ore_libere1}\nOre somn: {ore_somn1}\n"
          f"Calcul compensat cu ore/libere")
    print(f"TOTAL liber: {total_libere1} ore")

    # Calculăm orele pentru Serviciu normal
    ore_munca2 = 0
    ore_libere2 = 0
    ore_somn2 = 0

    for single_date in (start_date + timedelta(n) for n in range(numar_zile)):
        if single_date.weekday() < 5:  # Luni-Vineri
            ore_munca2 += 8  # 8 ore de muncă
            ore_somn2 += 8  # 8 ore de somn
            ore_libere2 += 8  # 8 ore libere
        else:  # Sâmbătă și Duminică
            ore_somn2 += 8  # 8 ore de somn
            ore_libere2 += 16  # 16 ore libere, fără muncă

    # Calculăm orele libere totale
    total_libere2 = ore_libere2 + ore_somn2  # Total liber = ore libere

    # Afișăm rezultatele pentru Serviciu normal
    print("\nRezultatele pentru Serviciu normal (8h/zi):")
    print(f"Numar de zile in interval: {numar_zile}")
    print(f"Numar de saptamani in interval: {numar_saptamani}")
    print(f"Numar de ore in interval: {ore_total}")
    print(f"Ore muncite: {ore_munca2}\nOre libere: {ore_libere2}\nOre somn: {ore_somn2}")
    print(f"TOTAL liber: {total_libere2} ore")


# Cerere de input pentru datele de început și de sfârșit
data_start = input("Introduceti data de început (dd.mm.yyyy): ")
data_sfarsit = input("Introduceti data de sfârșit (dd.mm.yyyy): ")

calculeaza_interval(data_start, data_sfarsit)
