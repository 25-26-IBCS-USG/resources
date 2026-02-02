# Simon Says

def main():

    print("Welcome to Simon Says!")

    m = "AWS"

    # indefinitely
    while True:

        print("Simon says, 'hop on one leg'")

        response = input("What should you do?")

        if response == "hop on one leg":
            print("You did it!")
            m = m + " gold star!"
        else:
            print("You are out!")
            break

        if response == "done":
            break


    # after the loop
    print("Thanks for playing")
    print(m)


    #will all be intented



if __name__ == "__main__":
    main()
