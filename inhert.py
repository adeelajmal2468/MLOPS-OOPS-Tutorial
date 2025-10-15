# #simple inheritance

# # Base Class  (Parent Class)

# class Animal: 
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound.")
        
# #Derived Class (Child Class)

# class Dog(Animal):
    
#     def __init__(self):
#         self.behaviour = "friendly" #constructor overloads
        
    
#     def speak(self):
#         print(f"{self.name} barks.") #Constructor overloads
        
#     def speak1(self):
#         print(f"{self.name} barks. She is very {self.behaviour}") #Constructor overloads


# #Create an instance of Animal

# animal = Animal("Cow")
# animal.speak() #Output: Generic Animal makes a sound.

# #Create an instance of Dog

# dog = Dog()
# # dog.speak() #Output: Lucy barks.

# dog.speak1()

#Super Keyword

#Base class

class Animal:
    def __init__(self):
        self.name = "Buddy"
        
    def speak(self):
        print(f"{self.name} makes a sound.")
    

# Derived Class

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed
    
    def speak(self):
        super().speak() #Call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

#Create an instance of Dog

dog = Dog("Golden Retriever")
dog.speak()

#Output:
#Buddy makes a sound.
#Buddy barks. It is a Golden Retriever.