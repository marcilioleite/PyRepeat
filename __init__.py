'''
# Insert Batch
#INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);
'''
import DbReaders
from string import maketrans

reader = DbReaders.DbInfoReader('127.0.0.1', 'root', '', 'sopjd')

tables = reader.get_table_names()

for table in tables:
    print "Table: %s" % table
    columns = reader.get_columns(table)
    for column in columns: 
        print "\tColumn: \n\t\tName: %s, Type: %s, Allow Nulls: %r, Key: %s, Default: %s, Auto Increment: %r" % (column['name'], column['type'], column['null'], column['key'], column['default'], column['auto_increment'])