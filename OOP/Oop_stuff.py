class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
#self is well established way of saying it's a ref to this class
    def switch_on(self):
        self.on = True


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

print(hamilton.on)      #the default init to on is false and a print here will return the default
hamilton.switch_on()    #flipping it on here
print(hamilton.on)      #calling it again will return the current state of the switch obj which is now Attribute

Kettle.switch_on(kenwood)
print(kenwood.on)       #this assigns a power to Kettle.kenwood obj and can be refed after this point the program.
print("-"*80)

kenwood.power = 1.5
print(kenwood.power)
#print(hamilton.power)  #this does NOT assign and therefor gives an error because it doesnt have a power variable

Kettle.power_source = "atomic" #this changes Kettle power_source to "atomic"
