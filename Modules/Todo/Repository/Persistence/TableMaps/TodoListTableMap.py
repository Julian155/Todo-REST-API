from Modules.Kernel.Repository.Persistence.TableMaps.AbstractTableMap import AbstractTableMap

class TodoListTableMap(AbstractTableMap):
    TABLE_NAME = 'todo_list'

    RELATED_DELETION_TABLES = [
        'todo_entry'
    ]

    COL_ID = 'id'
    COL_NAME = 'name'

    ENTRY_ENTITIES = 'entryEntities'        
