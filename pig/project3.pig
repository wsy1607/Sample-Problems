--load data
o = load 'scripts/orders.csv' using PigStorage(',') As (oid:int,sid:chararray,date:chararray,amount:int);
s = load 'scripts/sales.csv' using PigStorage(',') As (id:chararray,name:chararray);

--question 1: find the highest amount with name
o1 = group o by sid;
bo1 = foreach o1 generate group as sid, MAX(o.amount) as amount;
answer1 = join s by id, bo1 by sid;
dump answer1;

--question 2: find the highest amount with name and order id
o2 = group o by sid;
bo2 = foreach o2 generate group as sid, MAX(o.amount) as best;
bs2 = join o by sid, bo2 by sid;
bs2 = foreach bs2 generate o::sid as sid, o::amount as amount, bo2::best as best, o::oid as oid;
bs2 = filter bs2 by amount == best;
answer2 = join s by id, bs2 by sid;
dump answer2;
