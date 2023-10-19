-- 코드를 입력하세요
SELECT a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') as review_date
FROM rest_review b
JOIN member_profile a ON a.member_id = b.member_id
WHERE a.member_id = (
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC limit 1
    )
ORDER BY review_date, b.review_text
