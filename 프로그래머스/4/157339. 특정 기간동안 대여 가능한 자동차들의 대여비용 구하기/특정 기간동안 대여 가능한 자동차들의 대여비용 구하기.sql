SELECT a.car_id, a.car_type, (case when c.duration_type NOT IN ('90일 이상') THEN round((a.daily_fee*30)*(1-(c.discount_rate*0.01)),0) ELSE a.daily_fee*30 END) as fee
FROM car_rental_company_car a
JOIN car_rental_company_rental_history b ON a.car_id = b.car_id
JOIN car_rental_company_discount_plan c ON a.car_type = c.car_type
WHERE a.car_type IN ('SUV', '세단') and
    a.car_id NOT IN (
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE start_date BETWEEN '2022-11-01' AND '2022-11-30'
        OR end_date BETWEEN '2022-11-01' AND '2022-11-30'
        OR (start_date <= '2022-11-01' AND end_date >= '2022-11-30')
    )
    and duration_type like '30일 이상'
GROUP BY a.car_id
HAVING fee BETWEEN 500000 AND 2000000
ORDER BY fee DESC, car_type, car_id DESC