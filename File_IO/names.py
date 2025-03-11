# name = input("What's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
"""method-1"""
# names=[]                            #creating a list
# with open("names.txt","r") as file: #using 'with' so you don't have to use file.close()  
#     for line in file:                            
#         names.append(line.rstrip()) #appending list and adding text from names.txt file;line.rstrip() for deleting extra lines 

# for i in sorted(names, reverse=True):             #'sorted' for sorting names and 'reverse=true' is used for reverse function of sorted
#     print(f"Hello, {i}")



