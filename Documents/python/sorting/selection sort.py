arr=[3,7,1,24,52,31,16,8,9]
for i in range(len(arr)):
    mini=i
    for j in range(i,len(arr)):
        if(arr[mini]>arr[j]):
            mini=j
    arr[i],arr[mini]=arr[mini],arr[i]


print(arr)
            
