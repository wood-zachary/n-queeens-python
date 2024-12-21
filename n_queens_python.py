#A global list that stores valid queen positions with rows representing rows and values representing columns
queens = []
count = 1
cont = True

#Checks the validity of a new Queen placement
def checkValid(row, col):
    global queens, count, cont

    #initializes the validity of the position to true
    validity = True

    #Each queen is stored in a row. Checks if column or diagonal is already occupied.
    for r in range(len(queens)):
        if (queens[r] == col):
            validity = False
        if (abs(r - row) == abs(queens[r] - col)):
            validity = False
    
    return validity

#Prints the current solution
def printSolution(q, numCol):
    global queens, count, cont

    print("Solution " + str(count) + ":")

    #increments the counter
    count += 1

    #iterates through each row of the chess board
    for r in range (len(queens)):
        #iterates through each col of the chess board
        for c in range (numCol):
            if (queens[r] != c):
                print("O ", end="")
            else:
                print("X ", end="")
            
        print("")
    
    print("")

#Finds all valid queen positions by adding and removing queens, either reaching the final row or row -1
def recursiveQueens(numRows, numCols, currentRow):
    global queens, count, cont

    #base case: row -1 = no solutions left 
    if (currentRow == -1):
        print("finished")
    elif (currentRow == numRows):
        #print the current solution
        printSolution(queens, numCols)
        #removes the last queen, continuing the search
        del queens[-1]
    else:
        #checks each col for a valid queen position
        for c in range(numCols):
            if (checkValid(currentRow, c)):
                queens.append(c)

                #recursive call to begin checking the next row
                recursiveQueens(numRows, numCols, currentRow + 1)
        #after iterating through every col in the row, remove the last queen and return to the previous row
        if (len(queens) > 0):
            del queens[-1]
        



#Main program runner
def main():
    global queens, count, cont

    print("This is an n-by-m queens solution generator. I haven't used python "
    "in a solid 5 or 6 years, so I'm recreating this to warm up a little "
    "before starting ML. n<m. Generates all symmetries, not unique solutions")

    #While loops that runs the program until client terminates it
    while (cont):
        n = int(input("Number of rows: "))
        m = int(input("Number of columns: "))

        #Calls recursive function with n by m dimensions and starting row 1. MAYBE 0????
        recursiveQueens(n, m, 0)

        #Resets the solution counter
        count = 1

        #Asks if user would like to continue
        answer = input("Would you like to continue? Type n for no: ")

        if (answer[0] == "n"):
            cont = False

#Runs the program
main()