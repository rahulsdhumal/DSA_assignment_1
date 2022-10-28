# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

size_of_array=int(input("Enter size of array : "))
arr=[]
for i in range(0,size_of_array):
        element=int(input())
        arr.append(element)
print(arr)
given_num = int(input("Enter a number : "))
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == given_num:
            print((arr[i], arr[j]),end=" ") 