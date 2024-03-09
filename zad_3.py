class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Nieruchomość zlokalizowanam w {self.address}, " +
                f"posiadająca {self.area} m^2. Liczba pokoi: " +
                f"{self.rooms}. Cena wynosi {self.price} zł.")


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom zlokalizowany w {self.address}, posiadający " +
                f"{self.area} m^2. Liczba pokoi: {self.rooms}. " +
                f"Rozmiar działki: {self.plot} m^2. " +
                f"Cena wynosi {self.price} zł.")


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie zlokalizowane w {self.address}, " +
                f"posiadające {self.area} m^2. Liczba pokoi: " +
                f"{self.rooms}. Piętro {self.floor}. " +
                f"Cena wynosi {self.price} zł.")


cca = House(120, 6, 433000, "Katowice, katowicka 6", 400)
ccb = Flat(70, 4, 267000, "Chorzów, 1 maja 23", 3)

print(cca)
print(ccb)
