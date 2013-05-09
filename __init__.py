import MySQLdb

con = MySQLdb.connect('127.0.0.1', 'root', '')
con.select_db('sopjd')
cursor = con.cursor()

# Get all tables
#
cursor.execute('show tables')
tables = cursor.fetchall()
for table in tables:
    print "Table '%s'" % table
    # Get all columns from a table
    #
    cursor.execute("describe %s" % table)
    #num_fields = len(cursor.description)
    columns_metadata = [i[0] for i in cursor.description]
    print columns_metadata
    columns = cursor.fetchall()
    for column in columns:
        print column


# Insert Batch
#INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);