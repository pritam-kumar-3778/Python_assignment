# Create a dictionary where :
# Keys = Student name
# Values = Marks (Integers)
# Write a menu - based program where user presses a key - 
# (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want to perform on the dictionary
# A - Add a student
# B - Update marks
# C - Search for a student
# D - Display All students and marks

Student_dict = {
    "Pritam" : 90,
    "Pritesh" : 95,
    "Sritam" : 96,
    "Sakhi" : 100
}

print("***Operation guide***")
print("A - Add a student")
print("B - Update marks")
print("C - Search for a student")
print("D- Display All students and marks")
print("************************************")

operation = input("Enter key according to the operation : ")

if(operation == 'A'):
    print("Add a student")
    A1 = input("Enter name : ")
    A2 = int(input("Enter mark : "))
    Student_dict[A1] = A2
    print(Student_dict)

elif(operation == 'B'):
    print("Update marks")
    B1 = input("Enter Student name where you want to update mark : ")
    B2 = int(input("Enter marks : "))
    Student_dict.update({B1:B2})
    print(Student_dict)

elif(operation == 'C'):
    print("Search for a student")
    C1 = input("Enter student name for search : ")
    if(C1 in Student_dict):
        print(f"{C1} found with marks {Student_dict[C1]}")
    else:
        print(f"{C1} is not in dictonary")
elif(operation == 'D'):
    print("Display All students and marks")
    All_info = Student_dict.items()
    print(All_info)
else:
    print("Wrong Input")