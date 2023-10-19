SELECT user_id, nickname, CONCAT_WS(' ', city, street_address1, street_address2) AS '전체주소', CONCAT(SUBSTR(tlno, 1, 3), '-', SUBSTR(tlno, 4, 4), '-', SUBSTR(tlno, 8)) AS '전화번호'
FROM USED_GOODS_USER
WHERE user_id IN (
    select writer_id
    from used_goods_board
    group by writer_id
    having count(*) >= 3)
ORDER BY user_id DESC;