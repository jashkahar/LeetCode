# Write your MySQL query statement below
Select a1.machine_id, Round(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
From Activity a1 Join Activity a2 On a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
Where a1.activity_type = 'start' and a2.activity_type = 'end'
Group by machine_id