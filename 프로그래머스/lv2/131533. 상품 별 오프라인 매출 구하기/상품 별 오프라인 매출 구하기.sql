-- 코드를 입력하세요
SELECT p.product_code,sum(sales_amount)*p.price as sales
from product as p, offline_sale as o
where p.product_id=o.product_id
group by p.product_id 
order by sales desc,product_code asc;


