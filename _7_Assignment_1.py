# Q7. Write a program to convert prefix expression to infix expression.

def isOperator(x):
    if x == "+" or  x == "-" or x == "*" or x == "/":
        return True
    else:
        return False
def prefixToInfix(prefix):
    lst = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            lst.append(prefix[i])
            i -= 1
        else:
            str = "(" + lst.pop() + prefix[i] + lst.pop() + ")"
            lst.append(str)
            i -= 1
    return lst.pop()
if __name__=="__main__":
    str = input("Enter Prefix Expresion : ") # */+-ABCD+DE
    print("Infix : ",prefixToInfix(str))