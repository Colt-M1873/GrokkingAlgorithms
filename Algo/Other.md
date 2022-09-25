蓄水池抽样

https://leetcode.cn/problems/linked-list-random-node/solution/gong-shui-san-xie-xu-shui-chi-chou-yang-1lp9d/





布隆过滤器

























1. (a + b) % p = (a % p + b % p) % p （1）
2. (a - b) % p = (a % p - b % p) % p （2）
3. (a * b) % p = (a % p * b % p) % p （3）
4. a ^ b % p = ((a % p)^b) % p （4）

- 结合律：

  ((a+b) % p + c) % p = (a + (b+c) % p) % p （5）

((a*b) % p * c)% p = (a * (b*c) % p) % p （6）

- 交换律：

  (a + b) % p = (b+a) % p （7）

(a * b) % p = (b * a) % p （8）

- 分配律：

  ((a +b)% p * c) % p = ((a * c) % p + (b * c) % p) % p （9）







数位DP，记忆化搜索

LeetCode 上的**「902. 最大为 N 的数字组合」**



和 [788. 旋转数字](https://leetcode.cn/problems/rotated-digits/)

https://leetcode.cn/problems/rotated-digits/solution/xuan-zhuan-shu-zi-by-leetcode-solution-q9bh/

https://mp.weixin.qq.com/s/8Z7W4xVnKLL3fLpjN6zXXQ

https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/python-shu-wei-dpmo-ban-ti-by-981377660l-xtkb/



