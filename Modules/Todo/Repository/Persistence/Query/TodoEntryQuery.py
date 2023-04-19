from __future__ import annotations
from typing_extensions import Self
from Modules.Kernel.Repository.Persistence.Query.AbstractQuery import AbstractQuery
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Modules.Todo.Repository.Persistence.Query.TodoListQuery import TodoListQuery
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity as EntryEntity

class TodoEntryQuery(AbstractQuery):
    def __init__(self, parentQuery: AbstractQuery|None = None):
        super(TodoEntryQuery, self).__init__(EntryEntity(), parentQuery)

    def findOneByEntryId(self, todoEntryId: str) -> 'EntryEntity'|None:
        return self.findOneBy(EntryEntity.TABLE_MAP.COL_ID, todoEntryId)

    def findByFkTodoList(self, todoListId: str) -> list['EntryEntity']|None:
        return self.findBy(EntryEntity.TABLE_MAP.TODO_LIST_TABLE_NAME, todoListId)

    def find(self)-> list[EntryEntity]:
        return self.findAll()

    def endUse(self)-> 'TodoListQuery':
        return super().endUse()