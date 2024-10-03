from abc import ABC, abstractmethod

"""
aplicatie bancara
modalitati diferite de instantiere si apelare
Abstractizare
"""


class Plata(ABC):
    @abstractmethod
    def efectueaza_plata(self, suma):
        pass


class PlataCard(Plata):
    def efectueaza_plata(self, suma):
        print(f"Plata cu cardul de {suma} lei a fost efectuată.")


class PlataPayPal(Plata):
    def efectueaza_plata(self, suma):
        print(f"Plata cu PayPal de {suma} lei a fost efectuată.")


class PlataBitcoin(Plata):
    def efectueaza_plata(self, suma):
        print(f"Plata cu Bitcoin de {suma} lei a fost efectuată.")


def proces_plata(plata, suma):
    plata.efectueaza_plata(suma)


# Instantiere mod 1
plata_Card = PlataCard()
plata_paypal = PlataPayPal()
plata_bitcoin = PlataBitcoin()

# apelare Instantiere mod 1
proces_plata(plata_Card, 10)
proces_plata(plata_paypal, 20)
proces_plata(plata_bitcoin, 30)

# Apeluri polimorfe mod 2, functioneaza si fara existenta # Instantiere mod 1
proces_plata(PlataCard(), 100)
proces_plata(PlataPayPal(), 200)
proces_plata(PlataBitcoin(), 300)

# apelare mod 3, ce ajutorul # Instantiere mod 1
plata_Card.efectueaza_plata(11)
plata_paypal.efectueaza_plata(22)
plata_bitcoin.efectueaza_plata(33)

# apelare mod 4
plati = [PlataCard(), PlataPayPal(), PlataBitcoin()]
suma = 123
for plata in plati:
    plata.efectueaza_plata(suma)

# apelare mod 5
platileCard = PlataCard()
platileCard.efectueaza_plata(321)

platilePayPal = PlataPayPal()
platilePayPal.efectueaza_plata(432)

platileBitcoin = PlataBitcoin()
platileBitcoin.efectueaza_plata(543)

