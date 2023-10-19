-- 코드를 입력하세요
SELECT c.apnt_no, a.pt_name, a.pt_no, c.mcdp_cd, b.dr_name, c.apnt_ymd
FROM appointment c
JOIN doctor b ON b.mcdp_cd = c.mcdp_cd
JOIN patient a ON a.pt_no = c.pt_no
WHERE b.mcdp_cd = 'CS' AND b.dr_id = c.mddr_id AND
c.apnt_cncl_yn = 'N' AND date_format(c.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
ORDER BY c.apnt_ymd