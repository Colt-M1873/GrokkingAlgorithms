# 知识点：整数转list只需要加方括号[]而不能用list(),list()用于将字符串或者元组转化为列表

# 递归的快速排序
def QuickSort_recursive(arr:list):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    smallarr=[]
    bigarr=[]
    for i in range(1,len(arr)):
        if arr[i]<=arr[0]:
            smallarr.append(arr[i])
        else:
            bigarr.append(arr[i])
    return QuickSort_recursive(smallarr)+[pivot]+QuickSort_recursive(bigarr)


# 循环的快速排序
# https://visualgo.net/zh/sorting  跟着这里写一遍
def QuickSort_iterative(arr:list):
    return 


arr1=[1,5,8,43,1,8,4,3,19,87,1,9879,84,6,312,5,6,87,874,1]        
print(arr1)
print(QuickSort(arr1))

