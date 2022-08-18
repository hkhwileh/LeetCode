
(
select a.name as results  
from (
select u.name name , count(*) over(partition by m.user_id order by u.name ) as cnt
from MovieRating m join Users u on m.user_id = u.user_id 
    ) as a
group by a.name
order by cnt desc , 1
limit 1
)
union
(
select s.results
from (
select mm.title as results , (sum(m.rating)/count(*)) as avg_rating
from MovieRating m join Movies mm on m.movie_id = mm.movie_id
where left(m.created_at,7) ='2020-02'
group by 1
order by avg_rating desc , results
limit 1
) as s
)