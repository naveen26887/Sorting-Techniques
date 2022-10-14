arr=[3,7,1,24,52,31,16,8,9]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print(arr)
