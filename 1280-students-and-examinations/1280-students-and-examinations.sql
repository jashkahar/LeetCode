# Write your MySQL query statement below
Select Students.student_id, Students.student_name, Subjects.subject_name, Count(Examinations.subject_name) As attended_exams
From Students
Join Subjects 
Left Join Examinations on Students.student_id = Examinations.student_id and Subjects.subject_name = Examinations.subject_name
Group By 1,2,3
Order By 1,3