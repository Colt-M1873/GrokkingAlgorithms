https://zhuanlan.zhihu.com/p/64940290

https://www.geeksforgeeks.org/jump-search/?ref=lbp

https://xie.infoq.cn/article/996cf8899930ae467cc790035

Leetcode 240



## Binary Search

```java
static int binSearch(int[] a, int target){
    // a should be an ascending array
    int l=0,r=a.length,mid=(l+r)/2;
    while (l<r){
        mid=(l+r)/2;
        if (target<a[mid]){
            r=mid-1;
        }else if (target>a[mid]){
            l=mid+1;
        }else{
            return mid;
        }
    }
    return l;
}
```





