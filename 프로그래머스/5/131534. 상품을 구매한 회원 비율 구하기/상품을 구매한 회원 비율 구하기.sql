-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE,"%Y")
,DATE_FORMAT(SALES_DATE,"%m")
,COUNT(DISTINCT I.USER_ID)
,ROUND(COUNT(DISTINCT I.USER_ID)/                                                                                (SELECT COUNT(DISTINCT USER_ID)                                                        FROM USER_INFO                                                                        WHERE JOINED LIKE "2021%"),1)
FROM ONLINE_SALE S JOIN USER_INFO I ON
S.USER_ID=I.USER_ID
WHERE JOINED LIKE "2021%"
GROUP BY DATE_FORMAT(SALES_DATE,"%Y"),DATE_FORMAT(SALES_DATE,"%m")
ORDER BY DATE_FORMAT(SALES_DATE,"%Y"),DATE_FORMAT(SALES_DATE,"%m")
