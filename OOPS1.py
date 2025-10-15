#How do we initiate a class?

class employee:
    #special function/method/magical method/dunder method. Constructor
    def __init__(self):
        print("Started executing attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes have been initiated")
        
    
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")
        
            

#Creating an object/instance of the class
sam = employee()

sam.travel("Lahore") # Calling a function/method

# print(sam.salary) #printing attributes of class

# print(sam.id)

print(type(sam))