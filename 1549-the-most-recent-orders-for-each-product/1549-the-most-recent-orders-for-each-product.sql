with cte as  (select order_id , order_date , customer_id ,product_id , dense_rank() over(partition by product_id order by order_date desc) as rnk from Orders )


select p.product_name product_name , c.product_id product_id  , c.order_id order_id  , c.order_date  order_date 
from Products p join cte c on p.product_id = c.product_id
where c.rnk =1
order by 1 ,2 , 3