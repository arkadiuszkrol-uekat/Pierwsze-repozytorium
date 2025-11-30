class Property:
    def __init__(self,area,rooms: int,price,address):
        self._area=area
        self._rooms=rooms
        self._price=price
        self._address=address

    def __str__(self):
        return f"Area: {self._area} with {self._rooms} rooms for {self._price}$ on {self._address}"
    
class House(Property):
    def __init__(self,area,rooms: int,price,address,plot:int):
        super().__init__(area,rooms,price,address)
        self._plot=plot

    def __str__(self):
        return f"Area: {self._area} and plot: {self._plot} with {self._rooms} rooms for {self._price}$ on {self._address}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self._floor=floor

    def __str__(self):
        return f"Area: {self._area} with {self._rooms} rooms for {self._price}$ on {self._address} on floor {self._floor}"
    
Domek=House(140,5,100000,"Kwietna 5", 250)
print(Domek)
Mieszkanko=Flat(70,2,60000,"Armii 67",4)
print(Mieszkanko)