from abc import ABC, abstractmethod
from flask import session
from typing_extensions import Self

from Modules.Kernel.Repository.Persistence.TableMaps.AbstractTableMap import AbstractTableMap

class AbstractEntity(ABC):
    TABLE_MAP = AbstractTableMap()
    
    id = ''

    new = True
    deleted = False

    def getId(self) -> str:
        """
        :return str
        """

        return self.id

    def setId(self, id: str) -> None:
        """
        :param str id

        :return None
        """

        self.id = id
        
    def isNew(self) -> bool:
        """
        :return bool
        """

        return self.new

    def isDeleted(self) -> bool:
        """
        :return bool
        """

        return self.deleted

    def setNew(self, isNew: bool) -> None:
        self.new = isNew

    def setDeleted(self, isDeleted: bool) -> None:
        self.deleted = isDeleted

    def doSave(self)-> None:
        tableName = self.TABLE_MAP.TABLE_NAME
    
        session[tableName][self.id] = self.toDict()
        self.saveRelations()

    def doDelete(self, childEntities: list[Self]|None = None)-> None:
        tableName = self.TABLE_MAP.TABLE_NAME

        session[tableName].pop(self.id)
        self.deleteSelfSearchColumns()
        self.deleteRelatedEntities(childEntities)

    def saveRelations(self)-> None:
        tableName = self.TABLE_MAP.TABLE_NAME
        searchColumnNameAndValue = self.getSelfSearchColumnNameAndValue()
        
        if len(searchColumnNameAndValue) > 0:
            colName: str
            value: str
            for colName, value in searchColumnNameAndValue.items():
                if value not in session[tableName][colName]:
                    session[tableName][colName][value] = []
                
                session[tableName][colName][value].append(self.id)
                
    def deleteRelatedEntities(self, childEntities: list[Self]|None = None)-> None:
        if (not childEntities):
            return None
        
        for childEntity in childEntities:
            childEntity.delete()

    def deleteSelfSearchColumns(self)-> None:
        tableName = self.TABLE_MAP.TABLE_NAME
        searchColumnNameAndValue = self.getSelfSearchColumnNameAndValue()

        if len(searchColumnNameAndValue) > 0:
            colName: str
            value: str
            for colName, value in searchColumnNameAndValue.items():
                session[tableName][colName][value].remove(self.id)
            
                if len(session[tableName][colName][value]) == 0:
                    session[tableName][colName].pop(value)

    @classmethod
    @abstractmethod 
    def save(self)-> None:
        ...

    @classmethod
    @abstractmethod 
    def delete(self)-> None:
        ...

    @classmethod
    @abstractmethod 
    def getSelfSearchColumnNameAndValue(self)-> dict:
        ...

    @classmethod
    @abstractmethod 
    def fromDict(self, row: dict)-> Self:
        ...

    @classmethod
    @abstractmethod
    def toDict(self)-> dict:
        ...


    