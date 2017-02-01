mercedes = vehicle('red', "AWD", 'Y', .....)
mercedes.color
mercedes.move()
mercedes.get.color(self)

class Vehicle(Object):
    def__init__(self,color, transmission, abs, doors, model):
        self.color = color
        self.transmission =transmission
        pass

    def move(self): #class functions
        pass
    def get.color(self):   #accessors getters.... mutators/setters

        return self.color   #instance functions, ways to rcv and change the variables with the class


    def set.color(self, color):
        self.color = color      ##GETTERS FOR most classes, not necessrily setters
