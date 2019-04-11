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

### HOW TO ...

```
python create_tables.py
python etl.py
```