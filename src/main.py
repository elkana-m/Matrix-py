"""
    Developer:  Elkana Munganga
    Date:       02/08/2022
    File:       main.py
    Subjects:   Matrix multiplication, addition, division
"""


# global variables for row and column of the matrix
rowNum = 5
colNum = 5


# -------------------------------------------getMat Function--------------------------------------------
def getMat(matrx):
    # Function to get Matrix A and B
    
    matrx = []
    tmpMat = []

    

    # creating matrix
    for i in range(rowNum):
        tmpMat = []
        for j in range(colNum):
            tmpNum = float(input(f"Please enter numbers for your {rowNum} x {colNum} matrix: "))
            tmpMat.append(tmpNum)
        matrx.append(tmpMat)
        print()

    return matrx


# -------------------------------------------addMat Function------------------------------------------------
def addMat(matrxA, matrxB):
    # Function to add 5 x 5 matrix
    
    # Defining the length of addMat accordingly to the length of rows Matrix A and B
    addlsMat = [[0 for x in range(len(matrxA))] for n in range(len(matrxB))]
    for i in range(len(matrxA)):                  # Iterate through the rows of MatA
        for j in range(len(matrxB[0])):           # Iterate through the cols of MatB
            addlsMat[i][j] = matrxA[i][j] + matrxB[i][j]
        print()

    return addlsMat


# -------------------------------------------prodMat Function------------------------------------------------


def prodMat(matrxA, matrxB):
    # Function to multiply 5 x 5 matrix

    # Defining the length of prodMat accordingly to the length of rows Matrix A and B
    multMat = [[0 for x in range(len(matrxA))] for n in range(len(matrxB))]
    tempMult = []
    for i in range(len(matrxA)):                  # Iterate through the rows of MatA
        # prodMat = []
        for j in range(len(matrxB[0])):           # Iterate through the cols of MatB
            for k in range(len(matrxB)):          # Iterate through the rows of MatB
                multMat[i][j] += matrxA[i][k] * matrxB[k][j]
                # tempMult.append(MatA[i][k] * MatB[k][j])
        # prodMat.append(tempMult)
        print()

    return multMat




# -------------------------------------------multMatElement Function------------------------------------------------
def multMatElement(matrxA,matrxB):
    # Function to multiply matrix by integer
    
    # Defining the length of prodMat accordingly to the length of rows Matrix A and B
    multMat = [[0 for x in range(len(matrxA))] for n in range(len(matrxB))]
    tempMult = []
    for i in range(len(matrxA)):                  # Iterate through the rows of MatA
        for j in range(len(matrxA[0])):           # Iterate through the cols of MatB
            # multiply element of matrix A by 5
            multMat[i][j] = matrxA[i][j] * 5
        print()

    return multMat

# -------------------------------------------divideMat Function------------------------------------------------
def divideMat(matrx):
    # Function to divide 5 x 5 matrix
    divMat = []
    tempDiv = []
    for i in range(len(matrx)):                  # Iterate through the rows of MatA
        tempDiv = []
        for j in range(len(matrx[0])):           # Iterate through the cols of MatA
            for k in range(len(matrx)):          # Iterate through the rows of MatA
                # dividing element of matrix A by 5
                tempDiv.append(matrx[i][k] / 5)
        divMat.append(tempDiv)
        print()
        
    return divMat






# -------------------------------------------print Function------------------------------------------------
def printMat(mat):
    # Function to print Matrix
    # Input: list
    # Output: void

    print()
    # Loop to print matrix
    for i in range(rowNum):
        for j in range(colNum):
            print(mat[i][j], end=" ")
        print()
    


# -------------------------------------------Main Function------------------------------------------------
def main():

    matrixA = []
    matrixB = []

    
    print("\nNow, enter for Matrix A")
    A = getMat(matrixA)         # user enters data for Matrix A
    print("\nNow, enter for Matrix B")
    B = getMat(matrixB)         # user enters data for Matrix B

    print("Printing MatxA: ")
    printMat(A)                 # Displaying Matrix A
    print("\nPrinting MatxB: ")
    printMat(B)                 # Displaying Matrix B


    # addition Matrix of 5x5
    adding = addMat(A, B)
    print("\nAddition of 5 x 5 matrix")
    printMat(adding)                 

    # product Matrix of 5x5
    product = prodMat(A, B)
    print("\nProduct of 5 x 5 matrix")
    printMat(product)

    # multiply matrix elements by integer
    print("\nmultiply matrix elements by integer")
    multMatrxByint = multMatElement(A,B)
    printMat(multMatrxByint)

    # divide matrix elements my integer
    print("\ndivide matrix elements my integer")
    divMatrxByint = divideMat(A)
    printMat(divMatrxByint)

main()
