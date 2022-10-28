# Q2.Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

size_of_array=int(input("Enter size of array : "))
arr=[]
for i in range(0,size_of_array):
        element=int(input())
        arr.append(element)
print("Original array : ",arr)
start=0
end=len(arr)-1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print("Array after reversing : ",arr)