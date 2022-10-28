# Q3. Write a program to check if two strings are a rotation of each other?

def checkRotation(s1, s2, index, Size):
    for i in range(Size):
        if(s1[i] != s2[(index + i) % Size]):
            return False
    return True

s1 = input("Enter first string : ") # ABCDEFG
s2 = input("Enter second string : ") # DEFGABC
 
if(len(s1) != len(s2)):
    print("Given Strings are not rotations of each other.")
else:
    indexes = [] 
    Size = len(s1)
    firstChar = s1[0]
    for i in range(Size):
        if(s2[i] == firstChar):
            indexes.append(i)
 
    isRotation = False
    for idx in indexes:
        isRotation = checkRotation(s1, s2, idx, Size)
        if(isRotation):
            break
 
    if(isRotation):
        print("Given Strings are rotations of each other.")
    else:
        print("Given Strings are not rotations of each other.")