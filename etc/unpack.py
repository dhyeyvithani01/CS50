# def total(galleons,sickles,knuts):
#     return (galleons*17+sickles)*29+knuts

# coins=(100,50,25)
# coin={"galleons":200,"sickles":100,"knuts":50}

# print(total(*coins),"Knuts")#* for unpacking list&
# print(total(**coin),"Knuts")#** for unpacking dictionary


def f(*args,**kwargs):
    print("Names:",kwargs)

f(Galleons=100,sickles=50,knuts=25)