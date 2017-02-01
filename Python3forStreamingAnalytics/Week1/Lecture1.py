class animal:


    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x = self.x + x
        self.y = self.y + y

    def eat(self):
        print('eat')


    def createnoise(self):
        print('noise')

class dog(animal):  # gets all the attributes from animal class

    def __init__(self,x,y):
        super().__init__(x,y) ## calling super class , call the constructor of the base class

    def __repr__(self):
        return str(self.x) + " " + str(self.y)  #self.x and self.y refer to the self.x and self.y that are declared in the animal base class
    # repr converts class into a string. here it will return "1 2"

    def createnoise(self):
        print('woof')
        super().createnoise()
#instantiate a class, creating an object of the type of this class. create an instance

a = dog(1,2)
print(a)
mutt = dog(1,2)
mutt.createnoise()