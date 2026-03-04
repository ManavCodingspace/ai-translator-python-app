class Person:

    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g

    def talk(self):
        print("hi, i am", self.name)

    def vote(self):
        if self.age > 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

obj = Person("John", 20, "Male")
obj.talk()
obj.vote()

obj1 = Person("Rohan", 17, "Male")
obj1.talk()
obj1.vote()