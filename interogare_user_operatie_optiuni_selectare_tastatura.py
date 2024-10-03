while True:
    Operatie = int(input(f"Selectati operatiunea dorita: 1. Adunare, 2. Scadere \n"))
    if Operatie == 1:
        print("Ai ales adunare.")
        x = int(input(f"Introduce-ti x: "))
        y = int(input(f"Introduce-ti y: "))
        z = x + y
        print(f"Rezultatul adunarii este: {z}")
        continue
    if Operatie == 2:
        print("Ai ales scadere.")
        x = int(input(f"Introduce-ti x: "))
        y = int(input(f"Introduce-ti y: "))
        z = x - y
        print(f"Rezultatul scaderii este: {z}")
        continue
    else:
        print("Ai ales gresit, incearca din nou.")