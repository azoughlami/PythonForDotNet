def main():
    name = input("What is your name? ")
    some_method(name)


def some_method(name):
    if name.strip().lower() == "hmichael":
        print("Hello old friend!")
    else:
        print(f"Nice to met you {name} !")
    print("My name is python")


if __name__ == "__main__":
    main()
