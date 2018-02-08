--purchased on ios then gpl ever
select count(distinct a.userid)
from daily_revenue as a
inner join daily_revenue as b
on a.userid = b.userid
and a.date < b.date
and a.platform = 'ios'
and b.platform = 'gpl'

--purchased on ios then gpl directly
select count(distinct revenue.userid)
from daily_revenue as revenue
inner join (
  select a.userid, a.date as first_date, min(b.date) as next_date
  from daily_revenue as a
  inner join daily_revenue as b
  on a.userid = b.userid
  and a.date < b.date
  and a.platform = 'ios'
  group by 1,2) as temp
on revenue.userid = temp.userid
and revenue.date = temp.next_date
and revenue.platform = 'gpl'  
