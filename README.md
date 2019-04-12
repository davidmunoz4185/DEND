# DEND

### BEFORE ANYTHING ...

In order to make easier this project implementation, we have used docker containers to create our database.
Refer 2 the following links to make it work by docker-compose:

* https://www.docker.com/
* https://docs.docker.com/compose/

Once is done:

```
docker-compose up -d 
```

### SUMMARY ...

* sql_queries.py: set of sql instructions 2 drop, create and load postgres tables ...
* create_tables.py: set of python functions 4: creating database, droping tables and creating tables ...
* etl.py: once ddls have been executed, proceed to load data modelling ...

### DATABASE DIAGRAM ...

We can observe how the database diagram has been implemented:

![alt text](./sparkify_diagram.jpg "sparkify db Diagram")

### DOCUMENT PROCESS ...

__Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.__

The purpose of this database is joining the 2 dataset Sparkify Startup owns in order to get conclussions about the traffic on their application. With this, and taking into account the requirements, we could be able to obtain information with just querying one database.

__State and justify your database schema design and ETL pipeline.__

We have chosen star schema because there is not second level of dimension tables. Due to we need song and artist information in order to complete fact table, the first step is recover that information and store it in song and artis tables.

In a second step, we load fact and the rest of dimension tables from log data and by using recovered from song dataset.

### HOW TO ...

```
python create_tables.py
python etl.py
```

