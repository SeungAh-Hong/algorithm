-- 코드를 입력하세요
SELECT order_id, product_id, date_format(out_date, '%Y-%m-%d') AS out_date, (case when out_date <= '2022-05-01' then '출고완료' when out_date IS NULL then '출고미정' else '출고대기' end) AS '출고여부'
FROM FOOD_ORDER
ORDER BY order_id