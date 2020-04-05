class Kettle(object):

    def __init__(sellf, make, price):
        self.make = make
        self.price = price
        self.on = False

kenwood = Kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))
"""
Class: template for creating objects. All objects created using the same class
    will have the characteristics.
Object: an instance of a class.
Instantiate: creating an instance of the class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""
