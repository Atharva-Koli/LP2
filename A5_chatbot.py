# Assignment no.5
# Name : Atharva Koli  Roll No: C33301

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print("What a great name you have, {0}!".format(name))

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5, and 7 respectively.")
    
    rem3 = int(input("Remainder when divided by 3: "))
    rem5 = int(input("Remainder when divided by 5: "))
    rem7 = int(input("Remainder when divided by 7: "))
    
    for age in range(105):
        if age % 3 == rem3 and age % 5 == rem5 and age % 7 == rem7:
            print("Your age is {0}; that's a good time to start programming!".format(age))
            return
    
    print("Could not determine your age. Please ensure the remainders are correct.")

def count():
    print("Now I will show you that I can count to any number you want.")
    num = int(input("Enter a number: "))
    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To demonstrate the execution of a program.")
    print("4. To interrupt the execution of a program.")
    
    answer = 2
    guess = int(input("Enter the correct option number: "))
    
    while guess != answer:
        print("Please, try again.")
        guess = int(input("Enter the correct option number: "))
    
    print("Completed, have a nice day!\n")

def end():
    print("Congratulations! Have a nice day!\n")

# Running the chatbot
remind_name()
guess_age()
count()
test()
end()
