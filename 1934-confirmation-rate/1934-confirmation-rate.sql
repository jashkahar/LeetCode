# Write your MySQL query statement below
Select Signups.user_id, Coalesce(Round(Avg(action = 'confirmed'), 2), 0) as confirmation_rate
From Signups Left Join Confirmations on Signups.user_id = Confirmations.user_id
Group By Signups.user_id