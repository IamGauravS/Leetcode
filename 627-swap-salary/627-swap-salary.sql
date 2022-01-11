# Write your MySQL query statement below
update Salary 
set SEX = CASE sex 
WHEN 'f' THEN 'm' 
WHEN 'm' THEN  'f'
END
