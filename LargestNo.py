# Program to find the Largest Number in a array.
arr=[12,55,68,1,5,78,23,56,9]
n=len(arr)
max=arr[0]
for i in range(n):
    if(arr[i]>max):
        max=arr[i]
print("Largest Number is:",max) 