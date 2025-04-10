# Write your MySQL query statement below
Select employee_id
From Employees
Where salary < 30000
And manager_id not in (
    Select employee_id from Employees
)
Order By employee_id