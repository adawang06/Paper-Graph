import psycopg2
try:
   connection = psycopg2.connect(user="postgres",
                                  password="wangda10",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="citation_pairs")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from citation_pairs_schema.table1"
   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from citation_pairs_schema using cursor.fetchall")
   citation_pairs_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in citation_pairs_records:
       print("Id = ", row[0], )
       print("citations list = ", row[1], "\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


