# Write your MySQL query statement b
with cte as 
( select player_id, device_id,
 rank() over(partition by player_id order by event_date) rnk from Activity)
 

select player_id, device_id from cte where rnk=1

