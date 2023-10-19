-- 코드를 입력하세요
SELECT b.product_id, a.product_name, (a.price * b.amount) as total_sales
from food_product a
join (select product_id, sum(amount) as amount
     from food_order
     where date_format(produce_date, '%Y-%m') = '2022-05'
     group by product_id
     ) b on a.product_id = b.product_id
order by total_sales desc, b.product_id