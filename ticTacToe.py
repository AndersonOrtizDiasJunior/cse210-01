import os

gameBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def  cls():
    os.system('cls' if os.name=='nt' else 'clear')

def printGame():
    cls()
    for i in range(9):
        if validateMove(i):
            print(f"|{gameBoard[i]}|", end="")
        elif gameBoard[i] == "X":
            print(f"\033[96m|{gameBoard[i]}|\033[0m", end="")
        else:
            print(f"\033[93m|{gameBoard[i]}|\033[0m", end="")
        if (i+1) % 3 == 0:
            print("\n")

def validateMove(postion):
    return gameBoard[postion] != "O" and gameBoard[postion] != "X"

def checkForWinner():
    if (gameBoard[0] == gameBoard[4] and gameBoard[4] == gameBoard[8]) or (gameBoard[2] == gameBoard[4] and gameBoard[4] == gameBoard[6]):
            return gameBoard[4]

    for i in range(0,8,3):
        if (gameBoard[i] == gameBoard[i+1] and gameBoard[i+1] == gameBoard[i+2]):
            return gameBoard[i]

    for i in range (0,3):
        if (gameBoard[i] == gameBoard[i+3] and gameBoard[i+6] == gameBoard[i+3]):
            return gameBoard[i]   
    return ""

def checkForDrawn():
    for i in range (9):
        if gameBoard[i] != 'X' and gameBoard[i] != 'O':
            return False
    return True

def main():
    turn = 0
    winner = ""
    isDrawn = False
    while winner != "X" and winner != "O" and not isDrawn:
        player = "X"
        if turn % 2 != 0:
            player = "O"
        printGame()
        print(f"{player} Turn!")
        isInputValid = False
        userInput = ''
        while not isInputValid:
            userInput = int(input("Choose a position beetwen 1 and 9:\n"))
            if userInput > 0 and userInput < 10:
                isInputValid = True
            else:
                print("Invalid option!")
            if validateMove(userInput-1):
                isInputValid = True
            else:
                print("this case was already selected, please select an empty one!")
        gameBoard[userInput-1] = player    
        winner = checkForWinner()
        if winner == '':
            isDrawn = checkForDrawn()
        turn += 1
    if isDrawn:
        print("It's a drawn!")
    else:
        print(f"Winner is {winner}")

if __name__ == "__main__":
    main()