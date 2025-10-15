#How do we initiate a class?

class employee:
    #special function/method/magical method/dunder method. Constructor
    def __init__(self):
        print(id(self)) #id is location (address) of object which is stored in memory
        # print("Started executing attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("Attributes have been initiated")
        
    
    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is now travelling to Lahore")
        
            

#Creating an object/instance of the class
sam = employee()

sam.name = "Sam"

print(sam.name)

# Adeel = employee()

# print(id(sam)) # id will be same as self. Jo bhi object banata hain, self is that object itself which can access the attributes e.g id or salaray
# print(id(Adeel)) # self's id changes if it is called in a different variable.
# sam.travel() # Calling a function/method. self doesnt need to be defined here. Object is self i-e sam here.

# print(sam.salary) #printing attributes of class

# print(sam.id)

# print(type(sam))