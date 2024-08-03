class Headphones():
    def __init__(self, id, name, description, price, image):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image


class HeadphonesModel():
    def __init__(self):
        self.headphones : list[Headphones] = []
