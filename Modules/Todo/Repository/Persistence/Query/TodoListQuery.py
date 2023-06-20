from __future__ import annotations
from Modules.Kernel.Repository.Persistence.Query.AbstractQuery import AbstractQuery
from Modules.Todo.Repository.Persistence.TableMaps.TodoEntryTableMap import TodoEntryTableMap
from Modules.Todo.Repository.Persistence.Query.TodoEntryQuery import TodoEntryQuery
from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity

class TodoListQuery(AbstractQuery):
    def __init__(self, parentQuery: AbstractQuery|None = None):
        super(TodoListQuery, self).__init__(TodoListEntity(), parentQuery)

    def findOneByListId(self, todoListId: str)-> 'TodoListEntity'|None: 
        return self.findOneBy(TodoListEntity.TABLE_MAP.COL_ENTITY, todoListId)

    def mergeRelatedEntities(self)-> None:
        if self.childEntityCollection:
            for colName, childEntities in self.childEntityCollection.items():
                match(colName):
                    case TodoEntryTableMap.COL_FK_TODO_LIST_ID:
                        self.entity: 'TodoListEntity'
                        self.entity.setTodoEntryEntities(childEntities)
            
    def useTodoEntryQuery(self) -> 'TodoEntryQuery': 
        todoEntryQuery = TodoEntryQuery(self)
        self.childQueries[TodoEntryTableMap.COL_FK_TODO_LIST_ID] = todoEntryQuery

        return todoEntryQuery

    def find(self)-> list[TodoListEntity]:
        return self.findAll()
    