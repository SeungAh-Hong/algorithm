SELECT a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') as review_date
FROM member_profile a
JOIN rest_review b ON a.member_id = b.member_id
WHERE a.member_id = (
    SELECT member_id FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC limit 1
)
ORDER BY b.review_date, b.review_text