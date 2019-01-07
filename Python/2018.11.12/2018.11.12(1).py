class TestClass:
    name = "TEST"

    def __init__(self):
        print("TTTTTTTTTTTTTTTTTTTTTTTT")

    @staticmethod
    def static_method():
        print ("STATIC!!!!")
    

    def set_name(self,new_name):
        self.name = new_name
        print("SET NAME>>>" self.full_name)



    def full_name(self):
        return self.name + "FFFF"

    
    def get_name(self):
        print("QQQQQQQQQQQQQQQ")
        self.price(time)

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def __init__(self):
        super().__init__()
        print("My init!!!")


test = TestClass()
child = Child()

print("11111>>", child.get_name())

cmd = input("Input the function name>>>> ")

c = callable(test.get_name)
print("cccccccc>>", c)

getattr(test, cmd)()
getattr(TestClass, 'static_method')()