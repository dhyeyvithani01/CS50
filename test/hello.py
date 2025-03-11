def main():
    name = input("What's your name ? ")
    print(hello(name))

def hello(To="World"):
    return f"Hello, {To}"

if __name__ == "__main__":
    main()
    