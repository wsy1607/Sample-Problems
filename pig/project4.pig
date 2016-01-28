--this project is about using cassandra as a data source

rows = LOAD 'cassandra://demodb/users' USING PigStorage();
