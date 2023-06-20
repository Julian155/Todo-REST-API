from Modules.Kernel.Repository.Persistence.TableMaps.AbstractTableMap import AbstractTableMap

class TodoListTableMap(AbstractTableMap):
    TABLE_NAME = 'todo_list'

    COL_ID = 'id'
    COL_NAME = 'name'

    ENTRY_ENTITIES = 'entryEntities'        
