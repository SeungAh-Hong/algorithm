-- 코드를 입력하세요
SELECT HISTORY_ID, 
    round(DAILY_FEE * (DATEDIFF(h.END_DATE,h.START_DATE)+1)
    * (case 
    when DATEDIFF(END_DATE,START_DATE)+1 < 7 then 1
    when DATEDIFF(END_DATE,START_DATE)+1 < 30 then 0.95
    when DATEDIFF(END_DATE,START_DATE)+1 < 90 then 0.92
    else 0.85 end)) as "FEE"

from CAR_RENTAL_COMPANY_CAR as c 
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
    on c.CAR_ID = h.CAR_ID
    join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
    on c.CAR_TYPE = p.CAR_TYPE

where c.car_type = "트럭"

group by HISTORY_ID

order by FEE desc , HISTORY_ID desc

# SELECT b.HISTORY_ID, 
#     ROUND(a.daily_fee * (datediff(b.end_date, b.start_date) + 1)
#           * (case
#             when datediff(b.end_date, b.start_date) + 1 < 7 then 1
#             when datediff(b.end_date, b.start_date) + 1 < 30 then 0.95
#             when datediff(b.end_date, b.start_date) + 1 < 90 then 0.93
#             else 0.9 end), 0
#     ) as FEE

# FROM car_rental_company_rental_history b
# JOIN car_rental_company_car a ON a.car_id = b.car_id
# JOIN car_rental_company_discount_plan c ON a.car_type = c.car_type
# WHERE a.car_type = '트럭'
# GROUP BY HISTORY_ID
# order by 2 DESC, 1 DESC