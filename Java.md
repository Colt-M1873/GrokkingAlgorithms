[TOC]



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

reverse sort only for integers 

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







## String 

int to string

```java
String s=String.valueOf(i);
//or
String rankStr = rank+"";
//or
String s=Integer.toString(i);
```

string to int 

```java
Integer.valueOf(str1);
Integer.parseInt(str1);

```

get substring and concat with `+`

```java
str1.substring(0,5)+"concatcontent";
```

print integer as binary string

```java
System.out.println(Integer.toBinaryString(x));
```



String index： using charAt

```
str.charAt(index);
str.length();
```

string comparison: check if tow strings are equal,
do not use `==`, use `str.equals()`

```java
"Hello".equals(greetingstr)
"Hello".equalsIgnoreCase("hello")// ignore case
```

### empty array is not `null`

empty array is an actual object, i.e. `""` denotes an string object with length of 0 and no content

however  a string variable can also be `null` , that means it has not assigned with any object.



## scanner input

```java
Scanner in = new Scanner(System.in);
```

## file input

```java
Scanner in = new Scanner(Paths.get("niyflle.txt"), "UTF-8");
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







## Map Hashmap

https://stackoverflow.com/questions/6802483/how-to-directly-initialize-a-hashmap-in-a-literal-way

```java
Map<Integer, Integer> m = new HashMap<>();
m.put(1,2);
m.put(3,4);
m.get(3);
m.remove(3); // remove keypair
m.clear(); // delete all
m.size();
m.containsKey(1);//check if key in map
```







## HashSet

https://www.geeksforgeeks.org/initializing-hashset-java/

https://stackoverflow.com/questions/2041778/how-to-initialize-hashset-values-by-construction

initialize hashset with constructor

```
Set<String> h = new HashSet<>(Arrays.asList("a", "b"));
Set<Integer> rot = new HashSet<>(Arrays.asList(2,5,6,9));
```

```
// Import the HashSet class
import java.util.HashSet;

public class Main {
  public static void main(String[] args) {
    HashSet<String> cars = new HashSet<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("BMW");
    cars.add("Mazda");
    cars.contains("Mazda"); // in
    cars.remove("Volvo"); // del
    cars.size(); // len
    cars.clear(); // delete all
    System.out.println(cars);
  }
}
```



```java
for (String i : cars) {
  System.out.println(i);
}
```





check not null

```
System.out.println(Objects.nonNull(s));
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

## bit manipulaiton

bitwise and & logical and &&

`^` xor

`~` not

`<<` left move

`>>` right move

`>>>` right move fill with sign bit







java initialize 2d array

```java
List<List<Integer>> list = new ArrayList<List<Integer>>();
// or
List<List<Integer>> list = new ArrayList<>();

```

https://stackoverflow.com/questions/30401948/initialize-listlistinteger-in-java

```java
int[][] arr=new int[10][20]
```

找java2d数组的题练一练，2d数组如何添加



concat two arraylist   `.addAll()`

```java
ArrayList<String> arraylist3=new ArrayList<String>();

arraylist3.addAll(Arraylist1); // add first arraylist

arraylist3.addAll(Arraylist2); // add Second arraylist
```





char to string

```
Character.toString()
```

convert char to int

```java
char x = '9';
int y = x - '0'; // gives the int value 9
```

***modulo*** `10^9 + 7`.

```
int M=1000000007;
int ret;
```







## ArrayList

cannot index with `arr[i]`, must use `get` method

```java
ArrayList<Integer> numbers = new ArrayList<>(Arrays. asList(1, 2, 3, 4, 5, 6));
al.add(value)
al.add(insertIndx,value)
al.get(index)
al.remove(index)
al.size()
```





```
Integer arr[] = { 5, 6, 7, 8, 1, 2, 3, 4, 3 };
```

注意位运算和加减法的优先级，一直要带括号，否则会先算加减法



```
 ArrayList<String> names2 = new ArrayList<>();
names2.forEach(System.out::println);
```



Arraylist deep copy

https://stackoverflow.com/questions/42067086/how-do-i-make-a-deep-copy-of-an-arraylistinteger-in-java

```java
private ArrayList<Integer> makeDeepCopyInteger(ArrayList<Integer> old){
    ArrayList<Integer> copy = new ArrayList<Integer>(old.size());
    for(Integer i : old){
        copy.add(new Integer(i));
    }
    return copy;
}
```



or using constructor

```java
List<Integer> copy = new ArrayList<Integer>(list);
```



partial arraycopy 

```java
System.arraycopy(a,idx1,b,idx2,length);
```



### Array copy

```
b=Arrays.copyOf(a,a.length)
b=a.clone()
System.arraycopy(b,idx1,a,idx2,length)
```



https://www.baeldung.com/java-system-arraycopy-arrays-copyof-performance



interface

queue

https://www.liaoxuefeng.com/wiki/1252599548343744/1265121791832960

```java
Queue<String> q = new LinkedList<>();
```











Java Max/Min of array, primitive array

https://stackoverflow.com/questions/1484347/finding-the-max-min-value-in-an-array-of-primitives-using-java

```
import java.util.Arrays;

public class Test {
    public static void main(String[] args){
        int[] tab = {12, 1, 21, 8};
        int min = Arrays.stream(tab).min().getAsInt();
        int max = Arrays.stream(tab).max().getAsInt();
        System.out.println("Min = " + min);
        System.out.println("Max = " + max)
    }

}
```

java Math.max() and Math.min() are only for primitive types like int double of float, not wrapper classes like Integer









## Algo Implementation

Priority queue

```

```



## Types

primitive types 8: 4 integer 2 float 1 char 1 boolean

### Primitive type and Wrapper Class

int and Integer

char and Character

HashSet HashMap cannot contain primitive types



## 128 traps in java

cannot use `==` to compare wrapper class outer than [-128,127]

那么为什么在-128-127之间可以直接可以用==比较呢？

https://blog.csdn.net/peinanwei__/article/details/123377205

```java
package helloworld;

public class HelloWorld {
	public static void main(String[] args) {
		Integer a = 128;
		Integer b = 128;
		int c = 128;
		System.out.println(a==b);
		System.out.println(a==c);
		System.out.println(b==c);
		System.out.println(a.equals(b));
		return ;
	}
}
// output:
// false
// true
// true
// true
```







gin vue admin

guli mail





## static

https://www.geeksforgeeks.org/difference-between-static-and-non-static-method-in-java/





## final 

constant





Comment to doc

start with `/**` end with `*/`





## Core  Java Vol.1

p29 

> 关键字 class 表明 Java 程序中的全部内容都包含在类中。这里， 只 需要将类作为一个加载程序逻辑的容器，程序逻辑定义了应用程序的行为。在

p34

> Double.isNaN();
>
> double and BigDecimal

p42 Type cast

bollean to integer

> 不要在 boolean 类型与任何数值类型之间进行强制类型转换， 这样可以防止 发生错误。只有极少数的情况才需要将布尔类型转换为数值类型，这时可以使用条件表 达式 b ? 1:0

p49 string  empty string is not `null`

p50 methods of string   string api

p55 StringBuilder

p56 scanner

p82 `String args[]` 命令行参数

p84 methods of array / array  api 

### Chapter.4 OOP

relationship between classes

* dependenct
* aggregation 
* inheritance

使用静态工厂方法来表示构造器的调用？？？？

mutator method 更改器方法，会对原对象进行更改

只访问而不修改对象的方法称为访问器方法(accesor method)，例如`arr1.get(1)`

有些方法看似修改了内容，但实际上是返回了新对象而非对旧对象直接操作，例如`str1.toUppperCase()` ， 原对象内容是没变的



主力类 workhorse class

instance field equal to member variables?

p107 不要在构造器中定义和实例域冲突的变量名，否则构造器里的局部变量会覆盖实例域



p108 对于每个非静态的方法（也就是能访问这个对象本身的方法），都有一个隐式implicit参数，即是这个方法所归属的类对象，在方法内部可以直接使用变量名来访问类的实例域的变量（省略对这个类对象的指代），也可以用`this`来进行指代

p110 不要编写返回可变对象的引用的方法（即不要直接返回类内对象的引用），否则在类外能通过访问这个对象的引用来对类内的数据进行修改，封装性就被破坏了，出现了风险。正确的操作是在返回之前clone出一个新的对象，然后将新对象的引用返回出去，防止外界直接操作类内部的对象

p111 一个方法可以访问这个类的所有对象的私有域，而不仅限于这个方法所属的某个对象

p112 final实例域在构造时必须进行初始化，并且之后不可进行修改，有点const的意思

p112 静态域（即类内的静态变量，用static来定义）属于类，而不属于某个对象，静态变量该类的全体对象成员是共享的，因此静态变量又称类变量

p113 静态变量使用的比较少，但静态常量很常用，用static final来定义，例如Math类中的pi值，或者System.out

p114 静态方法，也是用static来定义，类似于Solidity中的pure，表示不对该类的任何内部实例域或者这个对象本身进行操作，类似于`Math.pow(x,a)` ，静态方法能访问静态域（即类变量）。

p114 能直接通过具体对象名来调用静态方法，但不建议，还是应当通过类名来调用，比如Math.pow(x,a)

p115 不必初始化任何对象就能直接调用静态方法，Math.pow(x,a)

p115 main 方法也是一个静态方法，每个类都可以有一个自己的main方法，这个特性常用于进行单元测，并且不对整个应用产生影响：只要单独运行某个class文件，就执行main方法，而在大型应用时执行整个应用的main方法所在的文件，其他class中的main方法就不会运行。

p118-119 对于所有类型，java方法在本质上全是按值调用call by value，即方法接收到的是传入参数值的一个拷贝，不能修改任何传入参数本身的内容。

但在具体体现上，传入基本类型和传入对象引用效果是不同的，对于int double这样的基本类型，传入方法后方法的任何操作不会影响原来的变量，因为方法只对其拷贝进行操作。

而对于对象引用，当对象引用作为方法的参数的时候，方法虽然也是对对象引用进行了拷贝，但因为拷贝后的对象引用和原来的对象引用在内存中指向的是同一个对象的地址，在方法内部通过拷贝的对象引用也能直接修改对象的内容，表现出来的就是在方法内部对对象进行修改了，原来的对象引用也被修改了，但实质上是因为方法内外的引用指向的是同一个对象。即java能直接通过对象引用在方法内部对对象进行操作。

p119 用交换两个对象的方法来证明了值调用，很精妙

拿Int和Integer尝试一下？







math.round()

https://stackoverflow.com/questions/37256550/difference-between-math-rint-and-math-round-in-java#:~:text=or%20an%20Infinity.-,Math.,s%20and%20returns%20double%20s.









install java api doc in local machine







## ++ 和 +1 的区别









## Servlet

method:

```java
service
doGet  // only process get
dpPost // only process post
```

req despatcher: the same url

request redirector: another url









## Counterintuitives of java

128 trap

string comparison, not using `==` but use `str1.equals(str2)` instead

array copy `int[] b = Array.copyOf(a,a.length)`partial array copy `System.arraycopy(a,idx1,b,idx2,length)`
