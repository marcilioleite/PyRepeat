import MySQLdb

con = MySQLdb.connect('127.0.0.1', 'root', '')
con.select_db('sopjd')
cursor = con.cursor()
cursor.execute('select * from itens')
rs = cursor.fetchone()

#num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print field_names