# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 155

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

# # lst.clear()
# print(lst)

# my_str = my_str.capitalize()
# print(my_str)

# a = "x"
# b = "y"

# print(a + b)

from OOPS_Project import chatbook

user1 = chatbook()

print(user1.id)

# chatbook.set_id(43) # Using static method directly rather than obj

# user_2 = chatbook()
# print(user_2.id)

# user_3 = chatbook()
# print(user_3.id)

# user_2 = chatbook()
# print(user_2.id)
# user_3 = chatbook()
# print(user_3.id)

# print(user1.__name)
# print(user1._chatbook__name) # Access the hidden attribute

# print(user1.get_name()) #get name
# user1.set_name("Agent A") #set name
# print(user1.get_name()) #Check whether name was set or not

# #Function vs Method

# lst = [1,2,3]

# #function

# a1 = len(lst)

# print(a1)


# user1 = chatbook() # Creating a Object


# #Calling a Method from a object
# user1.sendmsg()