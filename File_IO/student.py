students=[]

# with open("students.csv","r") as file:
#     for line in file:
#         name,house,home = line.rstrip().split(",")
#         student ={"name":name,"house":house,"home":home}
#         students.append(student)
"""method-1 for sorting by defing function"""
# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students,key=get_house,reverse=True): #here 'get house' is used without paranthesis because get_house is passed in sorted function
#     print(f"{student['name']} is in {student['house']}")


"""method-2 for sorting using lambda function"""

# for student in sorted(students,key=lambda student : student["name","home"]):
#     print(f"{student['name']} is in {student['house']}")


import csv



"""using reader method"""
# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#     """method-1"""
#     # for row in reader:
#     #     students.append({"name":row[0],"house":row[1],"home":row[2]})
#     """method-2"""
#     for name,house,home in reader:
#         students.append({"name":name,"house":house,"home":home})

choice = int(input("enter 1 to read file.\nenter 2 to write into file.\n"))
"""using Dictreader method"""
if choice==1:
    students=[]
    with open("students.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name":row['name'],"house":row['house'],"home":row['home']})

    for student in sorted(students,key=lambda student : student["name"]):
        if student['home']!='Unknown':
            print(f"{student['name']} is in {student['house']} and {student['name']} lives in {student['home']}.")
        else:
            print(f"{student['name']} is in {student['house']} and information about {student['name']}'s home is Unknown.")
elif choice==2:
    i=1
    while i!=0:
        name = input("Enter the name of student:")
        home = input("Enter the address of home:")
        house = input("Enter the name of house:")

        with open("students.csv","a",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["name","home","house"])
            writer.writerow({"name":name,"home":home,"house":house})
        i=int(input("\nEnter 1 to Enter details of another student\nEnter 0 to exit the program.\n"))