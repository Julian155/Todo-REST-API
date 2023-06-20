from __future__ import annotations
from typing_extensions import Self
from Modules.Kernel.Repository.Persistence.Query.AbstractQuery import AbstractQuery
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Modules.Todo.Repository.Persistence.Query.TodoListQuery import TodoListQuery

class TodoEntryQuery(AbstractQuery):
    def __init__(self, parentQuery: AbstractQuery|None = None):
        super(TodoEntryQuery, self).__init__(TodoEntryEntity(), parentQuery)

    def findOneByEntryId(self, todoEntryId: str) -> 'TodoEntryEntity'|None:
        return self.findOneBy(TodoEntryEntity.TABLE_MAP.COL_ENTITY, todoEntryId)

    def findByFkTodoList(self, todoListId: str) -> list['TodoEntryEntity']|None:
        return self.findBy(TodoEntryEntity.TABLE_MAP.COL_FK_TODO_LIST_ID, todoListId)

    def find(self)-> list['TodoEntryEntity']:
        return self.findAll()

    def endUse(self)-> 'TodoListQuery':
        return super().endUse()