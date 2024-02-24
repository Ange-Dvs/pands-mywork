# lab5.1.5_Read_in_Student_info.py 
# 
# Write a program that will read in the data for the data structure above, 
# ie. reads in a student’s name, then keeps reading in their modules and grades (until the user enters a blank module name),
#You can break this up into two parts:
#a. Just read in the module names until the user enters blank,
#b. Then read in the grade as well
#This program can just read in one student (and their module details) 


student = {}
student["name"] = input("Enter student's name: ")

modules = []
while True:
    course_name = input("Enter module course name: ")
    if course_name == "":
        break

    module_grade = input("Enter the grade for the module: ")

    modules.append({"course_name":course_name, "grade":module_grade})

student["modules"] = modules

print(student)