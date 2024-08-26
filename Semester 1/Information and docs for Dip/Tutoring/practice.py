class Person:
    #initialize = constructor
    def __init__(self, name, age): #paramters
        self.name = name #self.name = attribute
        self.age = age
        print("person is created")

    def walk(self):
        print("person is walking")
    
    def work(self):
        print("person is working")


person1 = Person('Alice', 40)
print(person1.age)
print(person1.name)
person1.walk()
person1.work()

person2 = Person('Max', 50)
print(person2.name)
print(person2.age)

#--------------
#functions
#parameter - argument

# def show_message(username): #definition
#     print("hi", username)
#     print("--- Welcome to the application ---")
#     print('Press 1, 2 or 3')

# #call
# name = "lucas"
# show_message(name)


#------------
# variable naming 
# new_item = snake case
# newItem = camel case
# print() = functions
# HOST = constants
# Person = classes

