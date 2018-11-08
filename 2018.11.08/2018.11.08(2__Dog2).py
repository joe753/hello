class Ai:
    def __init__(self,name):
        self.name = name
        if (self.name == "Ai_1"):
            print ("Ai_1 >>>  Hi! My name is" , self.name )
        elif (self.name == "Ai_2"):
            print ("Ai_2 >>>  Good Morning! My name is" , self.name)
    def speak (self):
        if (self.name == "Ai_1"):
            print ("Ai_1 >>>  Did you have breakfast?")
        
        cmd = input ("식사를 하셨습니까?  (Y / N)")
        
        if (cmd == 'Y' or 'y'):
            print ("Ai_2 >>>  yes! I've eaten just now.")
        elif (cmd == 'N' or 'n'):    
            print ("Ai_2 >>>  No, How about you?")
        
    
        

        
Ai_1 = Ai("Ai_1")
Ai_2 = Ai("Ai_2")

    
Ai_1.speak()
