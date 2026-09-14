def main():

    print("say hello")
    say_hello()
    print()


    print("say hello(name)")
    say_hello("Zoe")
    print()

    print("say hello(name, times")
    say_hello("Zoe",5)
    print()

    print("say hello(name, times,1,2,3,4")
    say_hello("Zoe",5,1,2,3,4)
    print()

    print("say hello(name, times,1,2,3,4, val=7, mode= prod")
    say_hello("Zoe",5,1,2,3,4, val=7, mode= "prod")
    print()


    #print("named args")
    #say_hello("Michael","Python", "C#", mode="prod", log=True)
    #print()


def say_hello(name='friend', times =1, *args, **kwargs):
    print(f"Hello {name} with time ={times}, args ={args}, kwargs ={kwargs}")




if __name__ == "__main__":
    main()

