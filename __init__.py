'''
# Insert Batch
#INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);
'''
import DbDiscovery
import DbChecker

discovery = DbDiscovery.InfoDiscovery('127.0.0.1', 'root', '', 'sopjd')
checker = DbChecker.TableChecker(discovery)

tables = discovery.get_table_names()

for table in tables:
    print "Table: %s" % table
    columns = discovery.get_columns(table)
    triggers = discovery.get_trigger_names(table)
    for column in columns: 
        print "\tColumn: \n\t\tName: %s, Type: %s, Allow Nulls: %r, Key: %s, Default: %s, Auto Increment: %r" % (column['name'], column['type'], column['null'], column['key'], column['default'], column['auto_increment'])
    print "Has Insert Trigger: %r" % checker.has_insert_trigger(table)
    print "Has Update Trigger: %r" % checker.has_update_trigger(table)
    #for trigger in triggers:
    #    print "\tTrigger: \n\t\t%s" % trigger
    