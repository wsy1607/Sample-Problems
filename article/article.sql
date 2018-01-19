--How many authors don't view all of their own articles?
select count(distinct author_id)
from (
  select
    author_id,
    count(distinct article_id) as article_count,
    sum(case when viewer_id = author_id then 1 else 0 end) as author_viewer_count
  from
    article_table
  group by 1)
where article_count = author_viewer_count

--How many authors don't view any of their own articles?
select count(distinct author_id)
from (
  select
    author_id,
    sum(case when viewer_id = author_id then 1 else 0 end) as author_viewer_count
  from
    article_table
  group by 1)
where author_viewer_count = 0
