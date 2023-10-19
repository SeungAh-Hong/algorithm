-- 코드를 입력하세요
SELECT a.flavor
FROM first_half a
JOIN (select flavor, sum(total_order) as total_order from july group by flavor) b ON a.flavor = b.flavor
order by (a.total_order + b.total_order) desc limit 3