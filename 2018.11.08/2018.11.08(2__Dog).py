class Dog:
    def __init__(self,name):
        self.name = name
        self.color = "red"
        print(self.name, "was Born")
    
    def speak(self):
        print("YELP!", self.name)

    def wag(self):
            print("dog's wag tail")
    
    def __del__(self):
            print("destroy!!")

puddle = Dog("puddle")
sheperd = Dog("sheperd")

class Puppy (Dog):
    def __init(self):
        self.name = "Puppy"
        print("Puppy was Born")
    
    def wag(self):
        print ("Puppy's wag tail")

# ###########################################3333
    def tto():
        print("ttoooooooooooo")

보리 = Puppy("보리")
보리.speak()
print (puddle.color)
print (보리.color)
