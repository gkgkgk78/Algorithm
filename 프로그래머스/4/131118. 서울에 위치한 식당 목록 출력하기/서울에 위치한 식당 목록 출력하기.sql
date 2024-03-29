-- 코드를 입력하세요
SELECT I.REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS,
ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO AS I , REST_REVIEW AS R
WHERE I.ADDRESS LIKE "서울%" AND I.REST_ID=R.REST_ID
GROUP BY I.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC