#1 Python basics and control Structures.
# WAP that takes a list of strings, filters out fruits with more than 5 characters using for loop and if statement, for each fruit print it's length
fruits = ["Apple","Mango","Orange","Banana","Guava"]
for fruit in fruits:  #this for loop will filters out fruits with more than 5 characters
    if len(fruit)>=5: 
        print(f"The fruit {fruit} has {len(fruit)} characters.")

#2 Write a function that takes a list of integers and a threshold value. Use a *lambda function inside filter() to return a list of numbers greater than the threshold. Test the function with a list [1, 5, 10, 3, 8] and threshold 5
def filter_greater_than(numbers, threshold):
    return list(filter(lambda x: x > threshold, numbers)) #anonymous function that checks if each number x is greater than the given threshold.
result = filter_greater_than([1, 5, 10, 3, 8], 5)         #filter() applies condition to every element inside list, since filter returns object we convert into list
print(result)                                             #Only element that satisfies the condition are kept

#4 Write a divide_numbers(a, b) function with exception handling: Handle division by zero and invalid input (non-numeric values).
def divide(x,y):
    try:
       return x/y
    except ZeroDivisionError :
        return "Error: division by zero not allowed"
    except TypeError :
       return "Error: Both inputs must be numbers."
print(divide(11,2))    #Valid input
print(divide("a",10))  #Invalid input
print(divide(10,0))    #Diviision by zero

#5 Write a Python program to:Create a text file "students.txt" with student names and marks.Read the file and print names of students with marks above 80.
#creating students.txt file in write mode("w")
with open("students.txt", "w") as file:  #with keyword ensures that the file is opened and closed automatically after use
    file.write("Tirth 85\n")
    file.write("Varad 72\n")
    file.write("Kavya 90\n")
    file.write("Hiya 65\n")
    file.write("kripa 95\n")
    file.write("Juee 99\n")
with open("students.txt", "r") as file:  #reading file
    for line in file:                    #reads file line by line
        name, marks = line.split()       #split() will split the string into 2 parts whenever theres a space
        if int(marks) > 80:
            print(name)