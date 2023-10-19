select year(b.sales_date) as year, month(b.sales_date) as month, a.gender, count(distinct(a.user_id)) as users
from user_info a
join online_sale b ON a.user_id = b.user_id
group by year, month, a.gender having gender is not null
order by year, month, a.gender