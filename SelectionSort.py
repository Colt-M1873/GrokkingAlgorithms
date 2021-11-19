# 知识点： 列表的.pop(index) pop和append一样是直接对原数组进行操作

def findSmallest(array):
    index=0
    smallest=array[index]
    for i in range(1,len(array)):
        if array[i]<smallest:
            smallest=array[i]
            index=i
    return index

def SelectionSort(arr:list):
    newArr=[]
    for i in range(0,len(arr)):
        smallestIndex=findSmallest(arr)
        newArr.append(arr.pop(smallestIndex))
    return newArr

arr1=[1,5,8,43,1,8,4,3,19,87,1,9879,84,6,312,5,6,87,874,1]        
print(arr1,findSmallest(arr1))
print(SelectionSort(arr1))