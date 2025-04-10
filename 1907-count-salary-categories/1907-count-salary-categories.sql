# Write your MySQL query statement below
Select 'Low Salary' AS category, Sum(Case When income < 20000 Then 1 Else 0 End) As accounts_count 
From Accounts

Union 

Select 'High Salary' AS category, Sum(Case When income > 50000 Then 1 Else 0 End) As accounts_count 
From Accounts

Union 

Select 'Average Salary' AS category, Sum(Case When income Between 20000 And 50000 Then 1 Else 0 End) As accounts_count 
From Accounts
