# Write your MySQL query statement below
Select name From Employee where id IN
(Select managerId from Employee Group by managerId
Having (Count(Distinct id) >= 5))