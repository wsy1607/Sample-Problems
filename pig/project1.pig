--load data
a = load 'scripts/actors.csv' using PigStorage(',') As (id:int,name:chararray,age:int);
m = load 'scripts/movies.csv' using PigStorage(',') As (id:int,title:chararray,year:int);
ma = load 'scripts/movieActors.csv' using PigStorage(',') As (aid:int,mid:int);

--question 1: who has movies in 2015 with age more than 35
m1 = filter m by year == 2015;
a1 = filter a by age > 20;
ma1 = join a1 by id, ma by aid;
answer1 = join ma1 by mid, m1 by id;
name1 = foreach answer1 generate name;
dump name1;

--question 2: who has movies in both 2012 and 2015 with age more than 35
a2 = filter a by age > 35;
m22012 = filter m by year == 2012;
m22015 = filter m by year == 2015;
ma2 = join a2 by id, ma by aid;
answer21 = join ma2 by mid, m22012 by id;
name21 = foreach answer21 generate name;
answer22 = join ma2 by mid, m22015 by id;
name22 = foreach answer22 generate name;
name2 = join name21 by name, name22 by name;
name2 = foreach name2 generate name21.name;
dump name2;
