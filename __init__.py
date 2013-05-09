import MySQLdb

con = MySQLdb.connect('127.0.0.1', 'root', '')
con.select_db('sopjd')
cursor = con.cursor()

# Get all tables
#
#cursor.execute('show tables')
#tables = cursor.fetchall()
#for table in tables:
#    print table 

# Get all columns from a table
#
#cursor.execute('select * from itens')
#num_fields = len(cursor.description)
#columns = [i[0] for i in cursor.description]
#for column in columns:
#    print column
