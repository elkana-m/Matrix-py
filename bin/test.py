"""
    Developer:  Elkana Munganga
    Date:       02/08/2022
    File:       test.py
    Subjects:   Matrix mult, div, add
"""


tempMat_A = []
tempMat_B = []

MatA = []
MatB = []

rowNum = 5                      # prompt the user to enter the number of rows first matrix
colNum = 5                      # prompt the user to enter the number of cols first matrix
# totNum = rowNum * colNum        # total numbers inide matrix



# ------------------------------------------- start of getMat--------------------------------------------
def getMat():
    # Function to get Matrix A and B
    pass
# creating matrix A
for i in range(rowNum):
    # tmpNum = random.randrange(5,100)                #random numbers should be entered by the user
    tempMat_A = []
    # print("Test tempMat_A ", tempMat_A)

    for j in range(colNum):
        tmpNum = float(input(f"Please enter numbers for your {rowNum} x {colNum} matrix A: "))
        tempMat_A.append(tmpNum)
    MatA.append(tempMat_A)
    print()




# creating matrix B
for i in range(rowNum):
    # tmpNum = random.randrange(5,100)                #random numbers should be entered by the user
    tempMat_B = []
    for j in range(colNum):
        tmpNum = float(input(f"Please enter numbers for your {rowNum} x {colNum} matrix B: "))
        tempMat_B.append(tmpNum)
    MatB.append(tempMat_B)
    print()
# ------------------------------------------- end of getMat------------------------------------------------


# ------------------------------------------- start of PrintMat--------------------------------------------
def printMat():
    # Function to print Matrix
    # Input: list
    # Output: void
    pass


# printing Matrix A
# print("Test Mat A: ",MatA)
print()
print("Printing Mat A: ")
# Loop to print matrix
for i in range(rowNum):
    for j in range(colNum):
        print(MatA[i][j], end=" ")
    print()




# printing Matrix B
# print("\nTest Mat B: ",MatB)
print()
print("Printing Mat B: ")
# Loop to print matrix
for i in range(rowNum):
    for j in range(colNum):
        print(MatB[i][j], end=" ")
    print()
# ------------------------------------------- end of PrintMat----------------------------------------------


# ---------------------------------------------- start of addMat--------------------------------------------

def addMat():
    # Function to add 5 x 5 matrix
    pass

# Defining the length of addMat accordingly to the length of rows Matrix A and B
addlsMat = [[0 for x in range(len(MatA))] for n in range(len(MatB))]
tempMult = []
for i in range(len(MatA)):                  # Iterate through the rows of MatA
    for j in range(len(MatB[0])):           # Iterate through the cols of MatB
        addlsMat[i][j] = MatA[i][j] + MatB[i][j]
    print()

# print("\nTest ProdMat ", prodMat)

# print add matrix
print("\nadd 5 x 5 matrix")
for i in range(rowNum):
    for j in range(colNum):
        print(addlsMat[i][j], end=" ")
    print()

# ---------------------------------------------- end of addMat----------------------------------------------


# ---------------------------------------------- start of prodMat--------------------------------------------

def prodMat():
    # Function to multiply 5 x 5 matrix
    pass

# Defining the length of prodMat accordingly to the length of rows Matrix A and B
multMat = [[0 for x in range(len(MatA))] for n in range(len(MatB))]
tempMult = []
for i in range(len(MatA)):                  # Iterate through the rows of MatA
    # prodMat = []
    for j in range(len(MatB[0])):           # Iterate through the cols of MatB
        for k in range(len(MatB)):          # Iterate through the rows of MatB
            multMat[i][j] += MatA[i][k] * MatB[k][j]
            # tempMult.append(MatA[i][k] * MatB[k][j])
    # prodMat.append(tempMult)
    print()

# print("\nTest ProdMat ", prodMat)

# print mult matrix
print("\nproduct of 5 x 5 matrix")
for i in range(rowNum):
    for j in range(colNum):
        print(multMat[i][j], end=" ")
    print()

# ---------------------------------------------- end of prodMat----------------------------------------------


# ---------------------------------------------- start of multMatElement--------------------------------------------

def multMatElement():
    # Function to multiply 5 x 5 matrix
    pass

# Defining the length of prodMat accordingly to the length of rows Matrix A and B
multMat = [[0 for x in range(len(MatA))] for n in range(len(MatB))]
tempMult = []
for i in range(len(MatA)):                  # Iterate through the rows of MatA
    for j in range(len(MatA[0])):           # Iterate through the cols of MatB
        # multiply element of matrix A by 5
        multMat[i][j] = MatA[i][j] * 5
    print()


# print mult matrix
print("\nmultiply matrix elements by integer")
for i in range(rowNum):
    for j in range(colNum):
        print(multMat[i][j], end=" ")
    print()

# ---------------------------------------------- end of prodMat----------------------------------------------


# ---------------------------------------------- start of divMat--------------------------------------------

def divideMat():
    # Function to divide 5 x 5 matrix
    pass

divMat = []
tempDiv = []
for i in range(len(MatA)):                  # Iterate through the rows of MatA
    tempDiv = []
    for j in range(len(MatA[0])):           # Iterate through the cols of MatA
        for k in range(len(MatA)):          # Iterate through the rows of MatA
            # dividing element of matrix A by 5
            tempDiv.append(MatA[i][k] / 5)
    divMat.append(tempDiv)
    print()



# print division matrix
print("\ndivision matrix by an integer")
for i in range(rowNum):
    for j in range(colNum):
        print(divMat[i][j], end=" ")
    print()

# ---------------------------------------------- end of prodMat----------------------------------------------
