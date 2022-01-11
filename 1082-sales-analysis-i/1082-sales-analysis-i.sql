# Write your MySQL query statement below
select seller_id from Sales group by seller_id having sum(price) >= ALL(select sum(price) from Sales group by seller_id)