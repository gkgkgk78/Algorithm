-- 코드를 입력하세요
SELECT distinct o.animal_id,o.name
from animal_outs as o, animal_ins as i
where o.animal_id not in(
select distinct animal_id
from animal_ins
)
order by o.animal_id;