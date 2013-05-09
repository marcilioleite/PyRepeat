import MySQLdb

'''
DbInfoReader is used to get description about a database and its tables.

@author: Marcilio
'''
class DbInfoReader(object):

    def __init__(self, server, user, pw, db):
        self.connection = MySQLdb.connect(server, user, pw)
        self.connection.select_db(db)
        self.cursor = self.connection.cursor()
        
    def get_table_names(self):
        self.cursor.execute('SHOW TABLES')
        fetch = self.cursor.fetchall()
        tables = [table[0] for table in fetch]
        return tables
    
    def get_columns(self, table):
        self.cursor.execute("DESCRIBE %s" % table)
        columns = []
        fetch = self.cursor.fetchall()
        for c in fetch:
            null = False if c[2] == 'NO' else True
            auto_increment = True if c[5] == 'auto_increment' else False
            key_type = None 
            if   c[3] == 'PRI': key_type = 'Primary'
            elif c[3] == 'MUL': key_type = 'Foreign'
                
            h = { 
                 'name': c[0],
                 'type': c[1], 
                 'null': null,
                 'key': key_type,
                 'default': c[4],
                 'auto_increment': auto_increment
            }
            columns.append(h)
        return columns