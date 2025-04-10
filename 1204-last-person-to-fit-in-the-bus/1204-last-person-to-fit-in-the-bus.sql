# Write your MySQL query statement below
Select a.person_name
From Queue a Join Queue b On a.turn >= b.turn
Group By 1
Having SUM(b.weight) <=1000
Order by 1 DESC
Limit 1
