# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def isOperator(x):
    if x == "+" or  x == "-" or x == "*" or x == "/":
        return True
    else:
        return False
def postToPre(post_exp):
    lst = []
    length = len(post_exp)
    for i in range(length):
        if (isOperator(post_exp[i])):
            oprator1 = lst[-1]
            lst.pop()
            oprator2 = lst[-1]
            lst.pop()
            temp = post_exp[i] + oprator2 + oprator1
            lst.append(temp)
        else:
            lst.append(post_exp[i])
    res = ""
    for i in lst:
        res += i
    return res
if __name__ == "__main__":
    post_exp = input("Enter Postfix Expresion : ") # AB-C+D/DE+*
    print("Prefix : ", postToPre(post_exp))