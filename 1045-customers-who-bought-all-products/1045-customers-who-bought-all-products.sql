select customer_id
from (
select c.customer_id as customer_id, count(distinct c.product_key) as cnt_product
from Customer c 
group by c.customer_id ) as s
where s.cnt_product = (select count(*) from Product)