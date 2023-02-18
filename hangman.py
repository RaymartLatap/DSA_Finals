import random

hangman = (
    """
       |
    """,
    """
       |
       0
    """,
    """
       |
       0
     --+--
    """,
    """
       |
       0
    \--+--
     
    """,
    """
       |
       0
    \--+--/
    """,
    """
       |
       0
    \--+--/
       |
    """,
    """
       |
       0
    \--+--/
       |
       |
    """,
    """
       |
       0
    \--+--/
       |
       |
      |
      | 
    """,
    """
       |
       0
    \--+--/
       |
       |
      | |
      | |
    """
)

Max_wrong = len(hangman)-1

Words = ('AMAZING','GOOD','WELCOME','ENJOY','ROUGH')

Word = random.choice(Words)

ans = "_"*len(Word)

wrong = 0
used = []

print(ans)

while wrong<Max_wrong and ans!=Word:
    
    guess = input("\nMake a guess: ")
    guess = guess.upper()
    if guess not in used:
        
        if guess in Word:
            new=""
            for i in range(len(Word)):
                if guess == Word[i]:
                    new = new+guess
                else:
                    new = new+ans[i]
            ans = new
            print(ans)
        else:
            print("\nWrong guess")
            wrong+=1
            print(hangman[wrong])
            print(ans)
    else:
        print('\n Already Guessed!!')
    used.append(guess)
    print('\nUsed: ',used)
    
if wrong == Max_wrong:
    print("\nGame Over!!, You lost the game")
    print("Correct word was: ", Word)
else:
    print("\nBooyah!! You guessed it correct")