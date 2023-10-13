SELECT factory_id, factory_name, address
FROM food_factory
WHERE ADDRESS LIKE '강원%'
ORDER BY factory_id ASC;