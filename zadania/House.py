import zadania.Property as prop


class House(prop.Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom zlokalizowany w {self.address}, posiadający " +
                f"{self.area} m^2. Liczba pokoi: {self.rooms}. " +
                f"Rozmiar działki: {self.plot} m^2. " +
                f"Cena wynosi {self.price} zł.")
