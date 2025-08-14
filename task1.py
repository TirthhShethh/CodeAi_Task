#1 Python basics and control Structures.
# WAP that takes a list of strings, filters out fruits with more than 5 characters using for loop and if statement, for each fruit print it's length
fruits = ["Apple","Mango","Orange","Banana","Guava"]
for fruit in fruits:  #filters out fruits with more than 5 characters
    if len(fruit)>=5: 
        print(f"The fruit {fruit} has {len(fruit)} characters.")