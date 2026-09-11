def main():
    print("Python iteration demo")

    # while True:
    #     name = input("Please enter your name: ")
    #
    #     if not name:
    #         break
    #
    #     print(f"Hello, {name}!")

    nums = [1, 5, 8, 10, 7, 2]  # <--- List<object>


    print()
    for n in nums:
        print(f"The next number is {n}.")

    # no for(i=0, i< len(nums), i++)

    x, y = 1, 2
    for idx, n in enumerate(nums, start=1):
        print(f"The {idx}th number is {n}.")

    print()

    for _ in range(1, 6):  # _ when not used in loop
        print("This time")

if __name__ == "__main__":
    main()
