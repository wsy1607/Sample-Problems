-- write a query to get actors who performed at least a movie on 1999 and 2010

select a.name
from actors as a
inner join movieActors as ma on a.actorId = ma.actorId
inner join movie as m on ma.movieId = m.movieId
where m.year in ('1999','2010') and a.name is not null
group by a.name
having count(distinct m.year) >= 2
