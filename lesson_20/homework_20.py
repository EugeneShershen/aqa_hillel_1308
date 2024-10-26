import psycopg2

from lesson_20 import queries_for_db as query


def create_connection(dbname, user, password, host, port):
    connector = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("\nConnected to the database successfully!\n")
    connector.autocommit = True

    return connector


try:
    connection = create_connection("online_store", "shershen", "sher",
                                   "localhost", "5432")

    cursor = connection.cursor()

    cursor.execute(query.create_table_category)
    cursor.execute(query.insert_into_category)

    cursor.execute(query.create_table_product)
    cursor.execute(query.insert_into_product)

    cursor.execute(query.select_join_product_and_category)

    result = cursor.fetchall()
    print("Result:")
    for thing in result:
        print(thing)

except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting to PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("\nDataBase connection is closed")
