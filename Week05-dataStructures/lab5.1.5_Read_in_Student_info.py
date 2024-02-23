# lab5.1.5_Read_in_Student_info.py 
# 
# Write a program that will read in the data for the data structure above, 
# ie. reads in a student’s name, then keeps reading in their modules and grades (until the user enters a blank module name),
#You can break this up into two parts:
#a. Just read in the module names until the user enters blank,
#b. Then read in the grade as well
#This program can just read in one student (and their module details) 

#
student_name = input('Please enter the student name: ')

# while x != "" or "q": 

modules = []

enter_module = input("Please enter your module name: ")

while enter_module != "":
    modules.append(enter_module)
    enter_module = input("Please enter your module name: ")                 

student = {
    "name": student_name,
    "modules": modules
}
print (f'Student: {student["name"]}')
for course in student["modules"]:
    print (f'Modules: {course["modules"]}')