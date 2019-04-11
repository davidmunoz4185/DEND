import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """ Creates sparkifydb database and user student to query it

    Returns:
        cur {psycopg2 cursor} -- Cursor to execute querys vs database
        conn {psycopg2 connection} -- Connection to sparkify database
    """

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 user=postgres password=YyjRCj0VfCgP port=7432")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("DROP USER IF EXISTS student;")
    cur.execute("CREATE USER student with encrypted password 'student';")
    cur.execute("ALTER USER student WITH SUPERUSER;")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student port=7432")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """ Drops all the tables defined in "drop_table_queries"

    Arguments:
        cur {psycopg2 cursor} -- Cursor to execute querys vs database
        conn {psycopg2 connection} -- Connection to sparkify database
    """

    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """ Creates all the tables defined in "create_table_queries"

    Arguments:
        cur {psycopg2 cursor} -- Cursor to execute querys vs database
        conn {psycopg2 connection} -- Connection to sparkify database
    """

    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():

    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
