with cte as (select log_id , row_number() over(order by log_id ) as row_num from logs)

select min(log_id) as start_id, max(log_id) as end_id  from (
select row_num , log_id 
from cte
) a
group by a.log_id - a.row_num

