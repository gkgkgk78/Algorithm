-- 코드를 입력하세요
SELECT book_id,author_name,DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
from book as b, author as a
where b.category="경제" and b.author_id=a.author_id
order by published_date asc;