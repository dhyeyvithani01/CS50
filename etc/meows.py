# def meow(n: int) -> str:
#     """
#     Meows n times.

#     :param n: Number of times of meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     :return: A string of n meows, one per line
#     :rtype: str
#     """
#     #this is a restructered text, markdown language used for documentation.
#     return "meow\n"*n

# number: int=int(input("Number: "))
# meows: str = meow(number)
# print(meows,end="")


import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n",default=1,help="number of times to meow",type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("Meow")