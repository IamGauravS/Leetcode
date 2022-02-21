# Write your MySQL query statement below
# select same_day/totaldays from (select count(order_date) as totaldays, count(case when order_date = customer_pref_delivery_date then 1 end) as same_day from Delivery) as temp

select round(count(case when order_date = customer_pref_delivery_date then 1 end)*100/count(order_date),2) as immediate_percentage from Delivery