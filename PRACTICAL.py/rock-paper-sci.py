import random as rd 


def pickComputerMove(number):
    if number >= 0 and number < 1/3:
        computerMove = "rock"
    elif number >= 1/3 or number < 2/3:
        computerMove = "paper"
    elif number >= 2/3 or number < 1:
        computerMove = "scissor"
    return computerMove

def playGame():
    
    number = rd.random()
    computerMove = pickComputerMove(number)
    choice = input("A\B\C: ")
    if choice == 'A':
        if computerMove == 'rock':
            print("Tie.")
        elif computerMove == 'paper':
            print("You lose")
        elif computerMove == 'scissor':
            print("You win")
        
    elif choice == 'B':
        if computerMove == 'rock':
            print("You win")
        elif computerMove == 'paper':
            print("You tie")
        elif computerMove == 'scissor':
            print("You lose")
       
    elif choice == 'C':
        if computerMove == 'rock':
            print("You lose")
        elif computerMove == 'paper':
            print("You win")
        elif computerMove == 'scissor':
            print("Tie")

print("Select your choice:")
print("A.Rock")
print("B.Paper")
print("C.Scissor")
count = 1
while count != 0:
    playGame()

