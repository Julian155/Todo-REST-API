from Modules.Kernel.Repository.Persistence.TableMaps.AbstractTableMap import AbstractTableMap

class TodoEntryTableMap(AbstractTableMap):
    TABLE_NAME = 'todo_entry'

    COL_ID = 'id'
    COL_NAME = 'name'
    COL_DESCRIPTION = 'description'
    COL_FK_TODO_LIST_ID = 'fkTodoListId'
        
