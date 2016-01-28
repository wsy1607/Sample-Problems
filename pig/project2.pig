--load data
c = load 'scripts/content.csv' using PigStorage(',') As (cid:int,type:chararray,tid:int,uid:int);

--question 1: the rank of all types of content (group by);
c1 = group c by type;
answer1 = foreach c1 generate group, COUNT(c);
dump answer1;

--question 2: compute the distribution of numbers of comments on photos (not null)
p2 = filter c by type == 'photo';
c2 = filter c by type == 'comment';
pc2 = join p2 by cid, c2 by tid;
pcg2 = group pc2 by $0;
pcg2 = foreach pcg2 generate group as cid, COUNT(pc2) as numberofcomments;
pcd2 = group pcg2 by numberofcomments;
answer2 = foreach pcd2 generate group as numberofcomments, COUNT(pcg2) as mumberofphotos;
dump answer2;

--question 3: compute the distribution of numbers of comments on photos (including null)
p3 = filter c by type == 'photo';
c3 = filter c by type == 'comment';
pc3 = join p3 by cid left outer, c3 by tid;
pc3 = foreach pc3 generate p3::cid as cid, c3::tid as tid;
--pc3 = foreach pc3 generate $0 as cid, $6 as tid;
pcg3 = group pc3 by cid;
pcg3 = foreach pcg3 generate group as cid, COUNT(pc3.tid) as numberofcomments;
pcd3 = group pcg3 by numberofcomments;
answer3 = foreach pcd3 generate group as numberofcomments, COUNT(pcg3) as mumberofphotos;
dump answer3;
--STORE answer3 INTO 'myoutput' USING PigStorage (',');
