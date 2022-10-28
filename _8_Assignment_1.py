# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def isBalanced(exp):
    res = True
    count = 0
    for i in range(len(exp)):
        if (exp[i] == '('):
            count += 1
        else:
            count -= 1
        if (count < 0):
            res = False
            break
    if (count != 0):
        res = False
    return res
if __name__ == '__main__':
    exp1 = input("Enter brackets : ") # ((()))()
    if (isBalanced(exp1)):
        print("Brackets are closed")
    else:
        print("Brackets are not closed")