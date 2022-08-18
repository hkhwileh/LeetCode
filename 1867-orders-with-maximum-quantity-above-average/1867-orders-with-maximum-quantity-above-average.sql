with cte as (
select order_id    , avg(quantity) over(partition by order_id) as avg_q , max(quantity) over(partition by order_id) as amx_q
from OrdersDetails
) 

select order_id
from cte 
where amx_q > (select max(avg_q) from cte )
group by 1
