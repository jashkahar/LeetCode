# Write your MySQL query statement below
Select name As results From(
    Select user_id, name, Count(*)
    From Users Join MovieRating USing (user_id)
    Group By 1,2
    Order By 3 Desc, 2 Asc
    Limit 1 
) users

Union All

Select title as results From(
    Select movie_id, title, Avg(rating)
    From Movies Join MovieRating USing (movie_id)
    Where Date_Format(created_at, "%Y-%m") = "2020-02"  
    Group By 1,2
    Order By 3 Desc, 2 Asc
    Limit 1 
) movies