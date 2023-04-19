from __future__ import annotations
from uuid import uuid4
from typing_extensions import Self
from Modules.Kernel.Repository.Persistence.AbstractEntity import AbstractEntity
from Modules.Todo.Repository.Persistence.TableMaps.TodoEntryTableMap import TodoEntryTableMap

class TodoEntryEntity(AbstractEntity):
    TABLE_MAP = TodoEntryTableMap()

    name = ''
    description = ''
    fkTodoListId = ''

    def getName(self) -> str:
        """
        :return str
        """

        return self.name

    def getDescription(self) -> str|None:
        """
        :return str|None
        """

        return self.description

    def getFkTodoListId(self) -> str:
        """
        :return str
        """

        return self.fkTodoListId

    def setName(self, name: str) -> None:
        """
        :param str name

        :return None
        """

        self.name = name

    def setDescription(self, description: str|None) -> None:
        """
        :param str|None description

        :return None
        """

        self.description = description

    def setFkTodoListId(self, todoListId: str) -> None:
        """
        :param str todoListId

        :return None
        """
        self.fkTodoListId = todoListId
    
    def fromDict(self, row: dict)-> Self:
        for key, value in row.items():
            match key:
                case self.TABLE_MAP.COL_ID:
                    self.id = value
                case self.TABLE_MAP.COL_NAME:
                    self.name = value
                case self.TABLE_MAP.COL_DESCRIPTION:
                    self.description = value
                case self.TABLE_MAP.COL_FK_TODO_LIST_ID:
                    self.fkTodoListId = value
    
        return self

    def toDict(self)-> dict:
        
        return {
            self.TABLE_MAP.COL_ID: self.id,
            self.TABLE_MAP.COL_NAME: self.name,
            self.TABLE_MAP.COL_DESCRIPTION: self.description,
            self.TABLE_MAP.COL_FK_TODO_LIST_ID: self.fkTodoListId
        }

    def save(self) -> None:
        if (not self.id):
            self.id = uuid4().hex

        self.doSave()
    
    def delete(self) -> None:
        self.doDelete()

    def getTableName(self)-> str:

        return self.TABLE_MAP.TABLE_NAME

    def getSelfSearchColumnNameAndValue(self)-> dict:
        return {
            self.TABLE_MAP.TODO_LIST_TABLE_NAME: self.fkTodoListId
        }

    def getFkRelations(self)-> dict:
        return {
            self.TABLE_MAP.TODO_LIST_TABLE_NAME: self.fkTodoListId
        }