def main():
    while True:
        text= input('Enter a numer: ')
        if not text:
            print('later...')
            break

        num = int(text)

        num_class = "small" if num < 100 else "huge"
        print(f"the number i {num_class}")

if __name__ == "__main__":
    main()