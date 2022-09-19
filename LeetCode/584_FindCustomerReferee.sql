# https://leetcode.com/problems/find-customer-referee/
# 2022年09月17日 17:00:05

# Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id<>2 OR referee_id IS NULL