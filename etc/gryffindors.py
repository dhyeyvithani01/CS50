students=[
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slythrin"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors =filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])