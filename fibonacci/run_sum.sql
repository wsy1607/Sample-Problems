with daily_kpi as (
  select to_date(event_date) as dt_pst, sum(kpi) as kpi
  from table
  where event_date > '2018-04-01'
  group by 1
)

select a.dt_pst,
       sum(distinct a.kpi) as daily_kpi,
       sum(b.kpi) as run_sum_kpi
from daily_kpi as a
inner join daily_kpi as b
on a.dt_pst >= b.dt_pst
group by 1
order by 1
