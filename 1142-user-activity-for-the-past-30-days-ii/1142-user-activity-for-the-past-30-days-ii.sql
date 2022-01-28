# Write your MySQL query statement below
select ifnull(round(avg(activity_count),2), 0.00) as average_sessions_per_user
from (
select count(distinct session_id) as activity_count from Activity where datediff('2019-07-27',activity_date) between 0 and 29 group by user_id
    ) tmp
    