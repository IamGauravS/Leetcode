# Write your MySQL query statement below
select s.buyer_id from Sales s join Product p on s.product_id = p.product_id group by s.buyer_id having sum(p.product_name='S8') > 0 and sum(p.product_name='iPhone') = 0

# select buyer_id from Sales group by buyer_id having ''