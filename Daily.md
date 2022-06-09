
# 2022

**3.05** 

206 反转链表

注意要从输入链表的第一个开始反转，如果从最后一个开始反转的话会造成链表出现循环。

自己想的方法是借助队列，空间复杂度高，需要遍历两遍

好方法是一遍结束，用temp变量来记录原链表的下一位，然后用curr和prev两个变量来进行反转

递归方法：


**3.06**

53 最大子序和

自己没想出来

好方法是DP，创建dp列表，从头开始记录当前能取得的最大值，而后返回dp表的最大值。


**3.10**
121 买股票 dp

**3.11**

21合并链表，循环法即反复横跳，递归法即每次输入最小

141环形链表，快慢指针

160相交链表，可能不等长但末尾部分是相等的，利用长度差。

**3.12**

206 反转链表 C++

138 复制带随机指针的链表 C++ 
    链表循环，计算长度
    hashmap `unordered_map<int, str> umap;` 类似于python字典

**3.13**

20 有效括号 Stack

1 两数相加 Hashmap


**3.14**
88 合并两个有序数组 没有想到更高级的方法，只用C++实现了冒泡排序

71 简化路径 

**3.15**

1249  栈 没有做到最简，用的比较笨的两次遍历

26 双指针

**3.16**

946 验证栈序列，py 判断逻辑复杂，要理清之后进一步精简。

**3.19**

125 有效回文序列

**3.20**

88 合并两个有序数组 冒泡排序py

**3.21**

88 合并两个有序数组 双指针，从后向前

141 环形链表 快慢指针C++

142 环形链表2 快慢指针C++ 加上一些数学推导

**3.22**

19 删除链表倒数第n个节点 双指针计数

237 删除节点，问题不严谨。


**3.23**

415 处理字符串

**3.24**

670 最大交换 

**3.25**
876 链表中点 双指针异常简单

**3.26**

409 最长回文 哈希表或者set

**3.27**
21 合并两个有序数组 CPP iterative recursive


**3.28**

234 回文链表 双指针 栈

23 合并K链表 recursive 参照21题

思路不清晰的话先想暴力法，直接想高级做法容易卡关，先把暴力做出来再考虑优化时间，有时候写着暴力就想到了更高级的解法。


**3.29**

61 旋转链表 18min

287 寻找重复数 用数组当哈希表，哈希表，sort()，set()，数组看作链表类似142，改进二分搜索，位操作， 共7到8种方法
    287是很有意思的一道题，明明是数组但是能用和环形链表一样的方式去考虑


**3.30**

74 搜索2d矩阵 二分法搜索


**4.02**

3


**4.04**

1721


**4.05**

11

**4.09**

347



**4.14**

700 二叉搜索树，二叉查找树 1用队列进行层序遍历，2递归，3用二叉搜索树的有序特性来比较大小

144 前序遍历 1递归，2用栈循环

145 后序遍历 1递归，2用栈循环反向输出

94 中序遍历 1递归，2循环


https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions

↑统一的前中后序遍历




**4.16**

168 excel表列名称 循环，递归


**4.17**

169 多数元素 摩尔投票算法

171  Excel表列序号 10进制变26进制

897 递增顺序搜索树 inorder traversal


**4.19**

99 恢复二叉搜索树 inorder

191 位1的个数   位操作，lambda，转字符串然后.count 

190 颠倒二进制位  转字符串然后翻转，位操作


**4.20**


173 二叉搜索树迭代器  拆开的inorder traversal


**4.22**

202 happy number Go数学解法

**4.23**

205 同构字符串 

**4.24**

217 python Go 字典


**4.28**

219 

python字典寻址比数组寻址快无数倍

**4.29**

226 py/go
实现stack数据结构

**4.30**

228 py/go



**5.01**

844 比较含退格的字符串 py

**5.02**

844 比较含退格的字符串 go 
go在函数中定义函数（nested function）要通过将内部函数赋值给从属于外部函数的一个变量来进行


905 数组按奇偶性排序 py/go
双指针
内置sorted改变key
位操作x&1和x%2是一样的，都能比较奇偶性，但位操作更快


**5.05**

1679 K和数对的最大数目 哈希表计数


Functionality is more important than elegance


**5.06**

581 连续的最短无序子数组 最短无序连续子数组

Functionality is more important than elegance

1047 删除字符串中所有相邻重复项

1209 删除字符串中所有相邻重复项

**5.19**

235 最小公共祖先

**5.20**

12 interger to roman

1 two sum  hash table

2 add two numbers



5 最长回文子串
https://leetcode.com/problems/longest-palindromic-substring/
647 所有回文子串
https://leetcode.com/problems/palindromic-substrings/
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/


**5.23**

146 LRU  =  hashmap + double linked list

**5.26**

496 Monotonic stack





```python
asd
```



```java
asdafadfrsgdf
```



```
asdaiksdhkajsd
```



