# https://leetcode.com/problems/customers-who-never-order/
# 2022年09月17日 17:10:08
# Write your MySQL query statement below
SELECT Customers.name AS 'Customers'
FROM customers
WHERE Customers.id NOT IN (
    SELECT customerId FROM Orders
)