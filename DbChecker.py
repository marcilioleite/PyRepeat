'''
TableChecker is used to inspect table finding or matching informations.

@author: Marcilio
'''
class TableChecker(object):

    def __init__(self, info_discovery):
        self.info_discovery = info_discovery
    
    '''
    Checks if a table has the Insert Trigger
    '''
    def has_insert_trigger(self, table):
        triggers = self.info_discovery.get_trigger_names(table)
        insert_trigger = "replica_%s_on_insert" % table
        return insert_trigger in triggers           
    
    '''
    Checks if a table has the Update Trigger
    '''    
    def has_update_trigger(self, table):
        triggers = self.info_discovery.get_trigger_names(table)
        update_trigger = "replica_%s_on_update" % table
        return update_trigger in triggers           
        