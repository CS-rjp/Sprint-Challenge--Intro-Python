# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

    # def __getattribute__(self, attr):
    #     def on_all(*args, **kwargs):
            
humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# for vehicle in vehicles:
#     # print drive() call on each vehicle
#     print(vehicle.drive())

# print_drive = [vehicle.drive() for vehicle in vehicles]


# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
# for human in humans:
#   if 'D' in humans[human].name[0]:
#       print(humans[human].name)

a = [human.name for human in humans if 'D' in human.name[0]]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# for human in humans:
#   if 'e' in humans[human].name[-1]:
#       print(humans[human].name)

b = [human.name for human in humans if 'e' in human.name[-1]]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
#Human(self.name[0][1]) = 'C' and/or 'D' and/or 'E' and/or 'F' and/or 'G'
# for human in humans:
#   if  human.name[0] >= "C" and human.name[0] <= 0:
#       print(human.name)
c = [human.name for human in humans if human.name[0] >= "C" and human.name[0] <= "G"] 
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# add 10 to each person's age and return all values
# human.age[0] + 10
d = [human.age for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
print(h)
