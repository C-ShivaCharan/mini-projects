import random
while True:
    n=random.randint(1,100)
    guess=1
    a=-1
    while(a!=n):
        a=int(input("Guess a number(1,100):"))
        if(a>n):
            print("Oh!..Your guess is high re-try with small number")
        elif(a<n):
            print("Oh!..Your guess is low re-try with a large number")
        guess=guess+1

    print(f"🎉 Lets gooo...you guessed {n} in {guess} attempts ")
    print("👋 Thanks for playing! See you next time.")

    play_again=input("Do u want to play it again? (Y/N):").lower().strip()
    if(play_again=="n"):
        break


