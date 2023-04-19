from Modules.Kernel.Repository.Persistence.TableMaps.AbstractTableMap import AbstractTableMap

class TodoEntryTableMap(AbstractTableMap):
    TABLE_NAME = 'todo_entry'
    TODO_LIST_TABLE_NAME = 'todo_list'

    TABLE_COLS = [
        'todo_list'
    ]
    
    RELATED_FK_TABLES = [
        'todo_list'
    ]

    COL_ID = 'id'
    COL_NAME = 'name'
    COL_DESCRIPTION = 'description'
    COL_FK_TODO_LIST_ID = 'fk_todo_list_id'
        
