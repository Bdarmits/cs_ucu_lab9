from copy import deepcopy

class FloweColor:
    black = '000000'
    white = 'FFFFFF'
    red = 'FF0000'

class Flower:
    def __init__(self, color, petals_num, price):
        if color not in (FloweColor.black, FloweColor.white, FloweColor.red):
            raise TypeError ( "Bad color")
        if type(price) not in (int, float) or price <= 0:
            raise TypeError ("Incorrect price")
        if type(petals_num) != int or petals_num <= 0:
            raise TypeError ("Petals num must be int and >= 0")
        self.color = color
        self.petals_num = petals_num
        self.price = price

class Tulip(Flower):
    def __init__(self, color, petals_num, price):
        self.type_name = "tulip"
        super().__init__(color, petals_num, price)

class Rose(Flower):
    def __init__(self, color, petals_num, price):
        self.type_name = "rose"
        super().__init__(color, petals_num, price)

class Chamomile(Flower):
    def __init__(self, color, petals_num, price):
        self.type_name = "chamonile"
        super().__init__(color, petals_num, price)

class FlowerSet:
    def __init__(self):
        self.set_list = []
        self.total_price = 0

    def add(self, flow_obj):
        if len(self.set_list) > 0 and flow_obj.type_name == self.set_list[0].type_name:
            self.set_list.append(flow_obj)
        elif len(self.set_list) == 0:
            self.set_list.append(flow_obj)

    def total_price(self):
        for i in self.set_list:
            self.total_price += i.price



class Bucket:
    def __init__(self):
        self.bucket_list = []
        self.total_price = 0

    def add(self, set_obj):
        self.bucket_list.append(set_obj)

    def total_price(self):
        for i in self.bucket_list:
            self.total_price += i.total_price


if __name__ == "__main__":
    f1 = Tulip('000000', 7, 10)
    f2 = Tulip('000000', 7, 14)
    f3 = Tulip('000000', 7, 3)
    f4 = Rose('000000', 7, 1)
    f5 = Chamomile('000000', 3, 2)
    s1 = FlowerSet
    s1().add(f1)
    s1().add(f3)
    s1().add(f2)
    s2 = FlowerSet
    s2().add(f4)
    s3 = FlowerSet
    s3().add(f5)
    b1 = Bucket
    b1().add(s1)
    b1().add(s2)
    b1().add(s3)
    print(b1().total_price)