-- https://leetcode.com/problems/recyclable-and-low-fat-products/
-- 2022年09月17日 16:54:30
# Write your MySQL query statement below
SELECT product_id FROM Products
WHERE low_fats='Y' AND recyclable='Y'