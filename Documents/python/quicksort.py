def quicksort(start,end,array):
    if(start<end):
        p=partition(start,end,array)
        quicksort(start,p-1,array)
        quicksort(p+1,end,array)

def partition(start,end,array):
    pivot_index=start
    pivot=array[pivot_index]
    while start<end:
        while start<len(array) and array[start]<pivot:
            start+=1
        while array[end]>pivot:
            end-=1
        if(start<end):
            array[start],array[end]=array[end],array[start]
    array[pivot_index],array[end]=array[end],array[pivot_index]
    return end
arr=[10,4,5,9,8,11,16,14,2,1]
q=quicksort(0,len(arr)-1,arr)
print(q)
