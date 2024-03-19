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
