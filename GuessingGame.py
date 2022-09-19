import random
abc = input("DO YOU WANT TO PLAY THE GUESSING GAME?").upper()
while abc == "YES":
    i=1
    stringgg="Welcome to guessing game"
    print(stringgg.center(100), "\n")
    print("You've got 3 chances to guess the number")
    #ans=int(input("Type YES to continue NO to exit")).uppper()
    answer = random.randint(0,10)
    print(answer)
    guess=int(input("Enter a number between 0-10: "))
    if(guess==answer):
        print("YOU GUESSED IT RIGHT")
    else:
        while(answer!=guess):        
            if(i<3):
                if(answer>guess):
                    print("GUESS HIGHER")
                    i=i+1
                    guess=int(input("Enter a number between 0-10: "))
                elif(answer<guess):
                    print("GUESS LOWER")
                    i=i+1
                    guess=int(input("Enter a number between 0-10: "))   
            else:
                print("YOU RAN OUT OF CHOICES")
                break
        else:
            print("YOU GUESSED IT RIGHT")
    abc = input("DO YOU WANT TO PLAY THE GUESSING GAME AGAIN?").upper()
else:
    print("PLEASE VISIT AGAIN")






