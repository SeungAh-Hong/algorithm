SELECT a.car_id, a.car_type, round((a.daily_fee * 30 * (1 - c.discount_rate*0.01)) , 0) as FEE
FROM car_rental_company_car a
JOIN car_rental_company_rental_history b ON a.car_id = b.car_id
JOIN car_rental_company_discount_plan c ON a.car_type = c.car_type
where a.car_type in ('세단', 'SUV') and c.duration_type = '30일 이상'
    and a.car_id not in (
    select car_id
    from car_rental_company_rental_history
    where start_date between '2022-11-01' and '2022-11-30'
    or end_date between '2022-11-01' and '2022-11-30'
    or (start_date <= '2022-11-01' and end_date >= '2022-11-30'))
group by a.car_id having fee between 500000 and 2000000
order by fee desc, car_type, car_id desc