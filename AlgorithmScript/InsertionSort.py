
# 什么是插入排序里的哨兵？

def InsertionSort(arr:list):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            temp=arr[i]
            j=i-1
            while j>=0 and arr[j]>temp:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=temp
    return arr