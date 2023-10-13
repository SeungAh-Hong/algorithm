-- 코드를 입력하세요
SELECT a.rest_id, a.rest_name, a.food_type, a.favorites, a.address, ROUND(AVG(b.review_score), 2) AS score
FROM REST_INFO A
JOIN REST_REVIEW B ON A.REST_ID = B.REST_ID
GROUP BY A.REST_ID
HAVING A.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, A.FAVORITES DESC
