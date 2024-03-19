import zadania.Property as prop


class Flat(prop.Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie zlokalizowane w {self.address}, " +
                f"posiadające {self.area} m^2. Liczba pokoi: " +
                f"{self.rooms}. Piętro {self.floor}. " +
                f"Cena wynosi {self.price} zł.")
