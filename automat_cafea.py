class Tonomat:
    def __init__(self):  # definim constructorul clasei
        self.tip = None
        self.cantitate = None
        self.intensitate = None
        self.arome = None

    # Metodă pentru selectarea tipului de băutură
    def selectie_bautura(self):
        print("Selectați băutura dorită:")
        print("1. Espresso")
        print("2. Cappuccino")
        print("3. Scurto")
        print("4. Lungo")
        print("5. Ceai negru")
        print("6. Ceai verde")
        optiune = input("Introduceți numărul opțiunii: ")
        if optiune == "1":
            self.tip = "Espresso"
        elif optiune == "2":
            self.tip = "Cappuccino"
        elif optiune == "3":
            self.tip = "Scurto"
        elif optiune == "4":
            self.tip = "Lungo"
        elif optiune == "5":
            self.tip = "Ceai negru"
        elif optiune == "6":
            self.tip = "Ceai verde"
        else:
            print("Opțiune invalidă. Alegeți din nou.")
            return self.selectie_bautura()  # Revine la selecția băuturii
        print(f"Ați selectat {self.tip}.")

    # Metodă pentru selectarea mărimii paharului
    def marime_pahar(self):
        print("Selectați mărimea paharului:")
        print("1. 100 ml")
        print("2. 150 ml")
        print("3. 200 ml")
        optiune = input("Introduceți numărul opțiunii: ")
        if optiune == "1":
            self.cantitate = "100 ml"
        elif optiune == "2":
            self.cantitate = "150 ml"
        elif optiune == "3":
            self.cantitate = "200 ml"
        else:
            print("Opțiune invalidă. Alegeți din nou.")
            return self.marime_pahar()  # Revine la selecția mărimii
        print(f"Ați selectat un pahar de {self.cantitate}.")

    # Metodă pentru selectarea intensității băuturii
    def intensitate_bautura(self):
        print("Selectați intensitatea băuturii:")
        print("1. Mică")
        print("2. Medie")
        print("3. Intenso")
        optiune = input("Introduceți numărul opțiunii: ")
        if optiune == "1":
            self.intensitate = "Mică"
        elif optiune == "2":
            self.intensitate = "Medie"
        elif optiune == "3":
            self.intensitate = "Intenso"
        else:
            print("Opțiune invalidă. Alegeți din nou.")
            return self.intensitate_bautura()  # Revine la selecția intensității
        print(f"Ați selectat o băutură cu intensitatea {self.intensitate}.")

    # Metodă pentru selectarea aromei
    def aroma_bautura(self):
        print("Selectați aroma băuturii:")
        print("1. Alune de pădure")
        print("2. Caramel")
        print("3. Caramel sărat")
        print("4. Vanilie")
        print("5. Irish flavor")
        print("6. Italiano")
        print("7. Cubaneza")
        print("8. Orientala")
        print("9. Fără aromă")
        optiune = input("Introduceți numărul opțiunii: ")
        if optiune == "1":
            self.arome = "Alune de pădure"
        elif optiune == "2":
            self.arome = "Caramel"
        elif optiune == "3":
            self.arome = "Caramel sărat"
        elif optiune == "4":
            self.arome = "Vanilie"
        elif optiune == "5":
            self.arome = "Irish flavor"
        elif optiune == "6":
            self.arome = "Italiano"
        elif optiune == "7":
            self.arome = "Cubaneza"
        elif optiune == "8":
            self.arome = "Orientala"
        elif optiune == "9":
            self.arome = "Fără aromă"
        else:
            print("Opțiune invalidă. Alegeți din nou.")
            return self.aroma_bautura()  # Revine la selecția aromei
        print(f"Ați selectat aroma {self.arome}.")

    # Metodă pentru lapte, care este exclusă dacă se selectează ceai
    def lapte(self):
        if "Ceai" in self.tip:  # Dacă băutura este ceai, nu se adaugă lapte
            print("Ceaiul nu conține lapte.")
        else:
            print("Selectați cantitatea de lapte:")
            print("1. 10 ml")
            print("2. 25 ml")
            print("3. 50 ml")
            print("4. Fără lapte")
            optiune = input("Introduceți numărul opțiunii: ")
            if optiune == "1":
                print("Ați adăugat 10 ml lapte.")
            elif optiune == "2":
                print("Ați adăugat 25 ml lapte.")
            elif optiune == "3":
                print("Ați adăugat 50 ml lapte.")
            elif optiune == "4":
                print("Fără lapte adăugat.")
            else:
                print("Opțiune invalidă. Alegeți din nou.")
                return self.lapte()  # Revine la selecția de lapte

    # Metodă pentru zahăr, care selectează automat 2 lingurițe pentru ceai
    def zahar(self):
        if "Ceai" in self.tip:  # Dacă băutura este ceai, se adaugă automat 2 lingurițe de zahăr
            print("Pentru ceai, se adaugă automat 2 lingurițe de zahăr.")
        else:
            print("Selectați cantitatea de zahăr:")
            print("1. 1 linguriță")
            print("2. 2 lingurițe")
            print("3. 3 lingurițe")
            print("4. Fără zahăr")
            optiune = input("Introduceți numărul opțiunii: ")
            if optiune == "1":
                print("Ați adăugat 1 linguriță de zahăr.")
            elif optiune == "2":
                print("Ați adăugat 2 lingurițe de zahăr.")
            elif optiune == "3":
                print("Ați adăugat 3 lingurițe de zahăr.")
            elif optiune == "4":
                print("Fără zahăr adăugat.")
            else:
                print("Opțiune invalidă. Alegeți din nou.")
                return self.zahar()  # Revine la selecția de zahăr

    # Metodă finală care prepară băutura și afisează selecția finală
    def prepara_bautura(self):
        print("\n---- Rezumatul selecțiilor dumneavoastră ----")
        print(f"Tip băutură: {self.tip}")
        print(f"Mărime pahar: {self.cantitate}")
        print(f"Intensitate: {self.intensitate}")
        print(f"Aromă: {self.arome}")
        print("\nSe prepară băutura... Vă rugăm așteptați.\n")
        print("Băutura dvs. este gata! Vă rugăm să o savurați!")


# Cod principal care rulează programul tonomatului de băuturi
def ruleaza_tonomat():
    tonomat = Tonomat()
    tonomat.selectie_bautura()
    tonomat.marime_pahar()
    tonomat.intensitate_bautura()
    tonomat.aroma_bautura()
    tonomat.lapte()
    tonomat.zahar()
    tonomat.prepara_bautura()


# Rulăm programul
ruleaza_tonomat()
