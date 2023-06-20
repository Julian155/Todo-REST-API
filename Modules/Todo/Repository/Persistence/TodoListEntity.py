from __future__ import annotations
from typing_extensions import Self
from uuid import uuid4
from Modules.Kernel.Repository.Persistence.AbstractEntity import AbstractEntity
from Modules.Todo.Repository.Persistence.TableMaps.TodoListTableMap import TodoListTableMap
from Modules.Todo.Repository.Persistence.Query.TodoEntryQuery import TodoEntryQuery as ChildTodoEntryQuery
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity

class TodoListEntity(AbstractEntity):
    TABLE_MAP = TodoListTableMap()

    id = ''
    name = ''

    todoEntryEntities: list['TodoEntryEntity']
    todoEntryEntities = []

    def getName(self) -> str:
        """
        :return str
        """

        return self.name

    def getTodoEntryEntities(self)-> list['TodoEntryEntity']:
        return self.todoEntryEntities

    def setName(self, name: str) -> None:
        """
        :param str name
 
        :return None
        """

        self.name = name

    def setTodoEntryEntities(self, entries: list['TodoEntryEntity']) -> None:
        self.todoEntryEntities = entries

    def fromDict(self, row: dict)-> Self:
        self.id = row[self.TABLE_MAP.COL_ID]
        self.name = row[self.TABLE_MAP.COL_NAME]
        
        return self
    
    def toDict(self, withRelation: bool = True)-> dict:
        entity = {
            self.TABLE_MAP.COL_ID: self.id,
            self.TABLE_MAP.COL_NAME: self.name
        }

        if withRelation and self.todoEntryEntities:
            entity[self.TABLE_MAP.ENTRY_ENTITIES] = []
            for todoEntryEntity in self.todoEntryEntities:
                entity[self.TABLE_MAP.ENTRY_ENTITIES].append(todoEntryEntity.toDict())

        return entity

    def save(self) -> None:
        if (not self.id):
            self.id = uuid4().hex

        self.doSave()

    def delete(self) -> None:
        childEntities = self.todoEntryEntities if self.todoEntryEntities else self.queryTodoEntryEntities()
        self.doDelete(childEntities)

    def queryTodoEntryEntities(self)-> list['TodoEntryEntity']|None:
        return ChildTodoEntryQuery().findByFkTodoList(self.id)

    def getTableName(self)-> str:

        return self.TABLE_MAP.TABLE_NAME
        
        