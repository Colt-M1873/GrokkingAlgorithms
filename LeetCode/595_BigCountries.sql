-- https://leetcode.com/problems/big-countries/?envType=study-plan&id=sql-i
-- 2022年09月17日 16:55:59

# Write your MySQL query statement below
SELECT name,population,area FROM World
WHERE area>=3000000 OR population>=25000000
