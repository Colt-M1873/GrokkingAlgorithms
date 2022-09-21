https://visualgo.net/en

排序算法对应的leetcode题：

https://cloud.tencent.com/developer/article/1876011

https://github.com/gaochengcheng/LeetCode/blob/master/LeetCode%E5%88%B7%E9%A2%98%E7%AC%94%E8%AE%B0%EF%BC%88%E6%8E%92%E5%BA%8F%E9%83%A8%E5%88%86%EF%BC%89.md

https://www.cnblogs.com/zhangwanying/p/9914941.html



| 排序方法 | 时间复杂度（平均） | 时间复杂度（最坏） | 时间复杂度（最好） | 空间复杂度 | 稳定性 |
| :------- | :---- | :-------------: | :-------------- | :------ | :----- |
| 冒泡排序 | O(n²)              |       O(n²)        | O(n)               | O(1)       | 稳定   |
| 选择排序 | O(n²)              |       O(n²)        | O(n²)              | O(1)       | 不稳定 |
| 插入排序 | O(n²)              |       O(n²)        | O(n)               | O(1)       | 稳定   |
| 希尔排序 | O(n^(1.3-2))       |       O(n²)        | O(n)               | O(1)       | 不稳定 |
| 归并排序 | O(nlogn)           |      O(nlogn)      | O(nlogn)           | O(n)       | 稳定   |
| 快速排序 | O(nlogn)           |       O(n²)        | O(nlogn)           | O(nlogn)   | 不稳定 |
| 堆排序   | O(nlogn)           |      O(nlogn)      | O(nlogn)           | O(1)       | 不稳定 |
| 计数排序 | O(n+k)             |       O(n+k)       | O(n+k)             | O(n)       | 稳定   |
| 桶排序   | O(n+k)             |       O(n²)        | O(n)               | O(n+k)     | 稳定   |
| 基数排序 | O(n*k)             |       O(n*k)       | O(n*k)             | O(n+k)     | 稳定   |





Bubble sort

```java
private void bubbleSort(int[] nums){
    int tmp,n=nums.length;
    for (int i=0;i<n;i++){
        for (int j=i+1;j<n;j++){
            if (nums[i]<nums[j]) {
                tmp=nums[i];
                nums[i]=nums[j];
                nums[j]=tmp;
            }
        }
    }
}
```

Selection Sort





Insertion Sort





Shell Sort













## Merge Sort













## Quick Sort

v1 using index as pivot, relatively complex and really slow

```java
private void quickSort(int[] arr, int left, int right){
    if (left<right){
        int pivot=partition(arr,left,right);
        quickSort(arr,left,pivot-1);
        quickSort(arr,pivot+1,right);
    }
}
private int partition(int[] arr, int left, int right){
    int pivot=left;
    int idx=pivot+1;
    for (int i=left+1;i<=right;i++){
        if (arr[i]>arr[pivot]){ // < for ascending
            swap(arr,i,idx);
            idx++;
        }
    }
    swap(arr,pivot,idx-1);
    return idx-1;
}

private void swap(int[] arr, int i, int j){
    int tmp=arr[i];
    arr[i]=arr[j];
    arr[j]=tmp;
}
```

v2 using value as pivot

https://www.youtube.com/watch?v=SLauY6PpjW4&ab_channel=HackerRank

```java
    private void quickSort(int[] arr, int left, int right){
        if (left<right){
            int pivot=partition(arr,left,right);
            quickSort(arr,left,pivot-1);
            quickSort(arr,pivot,right);
        }
    }
    private int partition(int[] arr, int left, int right){
        int pivot=arr[(left+right)/2];
        while (left<=right){
            while (arr[left]>pivot){ // < for ascending
                left++;
            }
            while (arr[right]<pivot){ // > for ascending
                right--;
            }
            if (left<=right){
                swap(arr,left,right);
                left++;
                right--;
            }
        }        
        return left;
    }
    
    private void swap(int[] arr, int i, int j){
        int tmp=arr[i];
        arr[i]=arr[j];
        arr[j]=tmp;
    }
```



## Counting Sort







Heap Sort







Search?

binary search



