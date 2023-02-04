answer = 5

print("please guess any number betwween 1 and 10: !")
guess = int(input("please enter number as ur guess: "))

if guess< answer :
    print("please guess higher")
    print("please try again,guess another num now")
    guess = int(input())
    if guess == answer:
        print("well done ,you guess it on this attempt")
    else:
        print("sorry u havent guess correctly this time also")   
elif guess > answer:
    print("please guess lower number")
    print("please try again,guess another num now")
    if guess == answer:
        print("well done, you got it correct on this attempt")
    else:
        print("sorry u havent guess correctly this time also")   
else:
    print("you got it right charm")    