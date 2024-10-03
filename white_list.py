import random

import time


# Funcție pentru generarea unei liste de mașini cu string-uri dinamice
def genereaza_lista_masini(judete, numar_masini):
    car_list = []
    for _ in range(numar_masini):
        judet_ales = random.choice(judete)  # Alege un județ din lista
        numar = random.randint(100, 999)  # Generăm un număr de 3 cifre
        cod = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))  # Generăm 3 litere aleatorii
        masina = f"{judet_ales}{numar}{cod}"  # Format: judet + număr + cod
        car_list.append(masina)
    return car_list


# Funcția de verificare a mașinilor
def verifica_masini(car_list):
    # Generăm 6 mașini care au acces (white list)
    white_list = random.sample(car_list, 6)

    # Obținem mașinile care nu au acces
    black_list = [masina for masina in car_list if masina not in white_list]

    # Combinăm și amestecăm mașinile într-un flux
    flux_masini = white_list + black_list
    random.shuffle(flux_masini)

    # Simulăm fluxul de mașini
    for masina in flux_masini:
        if masina in white_list:
            print(f"Mașina {masina} este pe white list. Bariera se ridică.")
        else:
            print(f"Mașina {masina} este pe black list. Acces refuzat.")

        # Așteptăm 1 secunda până la următoarea mașină (pentru testare putem reduce timpul)
        time.sleep(0.6)  # Aici am redus la 0.1 secunde pentru testare rapidă


# Testare: Generăm 24 mașini cu marci variate și le verificăm
judete = ['B', 'TL', 'TM', 'IS', 'IF', 'CJ', 'BV', 'BZ', 'SV', 'CT', 'MM', 'GL']
car_list = genereaza_lista_masini(judete, 24)

# Apelăm funcția pentru a simula verificarea mașinilor
verifica_masini(car_list)