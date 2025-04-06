# Write your MySQL query statement below
Select customer_id, Count(Distinct Visits.visit_id) as count_no_trans
From Visits Left Join Transactions On Visits.visit_id = Transactions.visit_id
Where Transactions.transaction_id is Null
Group by customer_id
