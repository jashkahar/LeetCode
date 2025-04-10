# Write your MySQL query statement below
 Select If(id < (Select Max(id) From Seat),
        If(id % 2 = 0, id-1, id+1),
        If(id % 2 = 0, id-1, id)) As id, student From seat
 Order By id