

``` java
import java.util.Arrays;
Arrays.sort(arr1);
String s=new String(arr1.length);// assert and initialization
System.out.println(score); // wrong
for (int num: arr1){
    System.out.print(num+",");
}

// array copy
int[] sorted = Arrays.copyOf(score,score.length);
```

length 

https://www.geeksforgeeks.org/length-vs-length-java/







Sort array

```java
Arrays.sort(arr1); 
```

reverse sort integer and int 

```
Arrays.sort(arr1,Collections.reverseOrder());//may cause error
```

https://stackoverflow.com/questions/1694751/java-array-sort-descending

> That will work fine with 'Array of Objects' such as Integer array but will not work with a primitive array such as int array.
>
> The only way to sort a primitive array in descending order is, first sort the array in ascending order and then reverse the array in place. This is also true for two-dimensional primitive arrays.





int and Integer

Difference between an Integer and int in Java with Examples

https://www.geeksforgeeks.org/difference-between-an-integer-and-int-in-java/#:~:text=In%20Java%2C%20int%20is%20a,and%20manipulating%20an%20int%20data.



array reverse

```java
static void reverse(int[] a){
    int i,tmp,n=a.length;
    for (i=0;i<n/2;i++){
        tmp=a[i];
        a[i]=a[n-1-i];
        a[n-1-i]=tmp;
    }
    // for (int num: a){
    //     System.out.print(num+",");
    // }
}
```



array copy/ copy array

```java
// array copy
int[] sorted = Arrays.copyOf(score,score.length);
//or
int[] copiedArray = array1.clone();
```





array and ArrayList

| **S.No.** | **Array**                                                    | **Arraylist**                                                |
| :-------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1.        | Here we can’t revise the length of the array once constructed. | In ArrayList, we can revise the length of the array.         |
| 2.        | An array can hold primitives and objects both in Java.       | ArrayList can only hold objects, not primitives.             |
| 3.        | It can either be single-dimensional or multidimensional.     | It can be only single-dimensional                            |
| 4.        | Through the length keyword, we can determine the total size of an array. | Through the size() method, we can determine the size of an ArrayList. |
| 5.        | Array is static.                                             | ArrayList is dynamic and can be modified the size whenever needed. |
| 6.        | It is faster than ArrayList due to its static behaviour.     | It is slower as compared to the Array due to its dynamic behaviour. |

ArrayList append, foreach and lambda

```java
import java.util.ArrayList;
import java.util.function.Consumer;

public class Main {
  public static void main(String[] args) {
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    numbers.add(5);
    numbers.add(9);
    numbers.add(8);
    numbers.add(1);
    Consumer<Integer> method = (n) -> { System.out.println(n); };
    numbers.forEach( method );
  }
}
```









int to string

```java
String s=String.valueOf(i);
//or
String rankStr = rank+"";
//or
String s=Integer.toString(i);
```



binary search

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



print array

```java
for (int num: array1){
	System.out.print(num+",");
}
```







Map Hashmap

```java
Map<Integer, Integer> map = new HashMap<>();
```



Priority queue and Comparator

https://www.liaoxuefeng.com/wiki/1252599548343744/1265120632401152

```java
public class Main {
    public static void main(String[] args) {
        Queue<User> q = new PriorityQueue<>(new UserComparator());
        // 添加3个元素到队列:
        q.offer(new User("Bob", "A1"));
        q.offer(new User("Alice", "A2"));
        q.offer(new User("Boss", "V1"));
        System.out.println(q.poll()); // Boss/V1
        System.out.println(q.poll()); // Bob/A1
        System.out.println(q.poll()); // Alice/A2
        System.out.println(q.poll()); // null,因为队列为空
    }
}

class UserComparator implements Comparator<User> {
    public int compare(User u1, User u2) {
        if (u1.number.charAt(0) == u2.number.charAt(0)) {
            // 如果两人的号都是A开头或者都是V开头,比较号的大小:
            return u1.number.compareTo(u2.number);
        }
        if (u1.number.charAt(0) == 'V') {
            // u1的号码是V开头,优先级高:
            return -1;
        } else {
            return 1;
        }
    }
}

class User {
    public final String name;
    public final String number;

    public User(String name, String number) {
        this.name = name;
        this.number = number;
    }

    public String toString() {
        return name + "/" + number;
    }
}
```

https://leetcode.com/problems/relative-ranks/discuss/1194733/java-priority-queue-solution-o(nlogn)-91faster

```java
 PriorityQueue<Integer> pq = 
            new PriorityQueue<>((a,b)->score[b]-score[a]);
```

lambda expression `(a,b)->score[b]-score[a]` 

 lambda expression example

```java
// 1. 不需要参数,返回值为 5  
() -> 5  
  
// 2. 接收一个参数(数字类型),返回其2倍的值  
x -> 2 * x  
  
// 3. 接受2个参数(数字),并返回他们的差值  
(x, y) -> x – y  
  
// 4. 接收2个int型整数,返回他们的和  
(int x, int y) -> x + y  
  
// 5. 接受一个 string 对象,并在控制台打印,不返回任何值(看起来像是返回void)  
(String s) -> System.out.print(s)
```













































interface

queue

https://www.liaoxuefeng.com/wiki/1252599548343744/1265121791832960

```java
Queue<String> q = new LinkedList<>();
```















## Algo Implementation

Priority queue

```

```

