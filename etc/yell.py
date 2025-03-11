def main():
    yell("This","is","cs50")

def yell(*words):
    # uppercased = map(str.upper,words)#using map() function
    uppercased = [word.upper() for word in words]#using list comprehensions
    print(*uppercased)


if __name__ == "__main__":
    main()