from abc import ABC, abstractmethod
from flask import session
from typing_extensions import Self

from Modules.Kernel.Repository.Persistence.TableMaps.AbstractTableMap import AbstractTableMap

class AbstractEntity(ABC):
    TABLE_MAP = AbstractTableMap()
    
    id = ''
    
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

    def doSave(self)-> None:
        entityData = self.toDict()
        session[self.TABLE_MAP.TABLE_NAME][self.TABLE_MAP.COL_ENTITY][self.id] = entityData
           
        self.saveSearchData(entityData)

    def doDelete(self, childEntities: list[Self]|None = None)-> None:

        session[self.TABLE_MAP.TABLE_NAME][self.TABLE_MAP.COL_ENTITY].pop(self.id)
        
        self.deleteSearchData()
        self.deleteRelatedEntities(childEntities)
             
    def saveSearchData(self, entityData: dict)-> None:
        colName: str
        value: str
        for colName, value in entityData.items():
            if value and self.doesSearchColumnExistInTable(colName):
                self.createListIfValueDoesNotExist(colName, value)
                
                if self.id not in session[self.TABLE_MAP.TABLE_NAME][colName][value]:
                    session[self.TABLE_MAP.TABLE_NAME][colName][value].append(self.id)
                
    def deleteSearchData(self)-> None:
        for colName, value in self.toDict().items():
            if value and self.doesSearchColumnExistInTable(colName):
                session[self.TABLE_MAP.TABLE_NAME][colName][value].remove(self.id)
            
                if len(session[self.TABLE_MAP.TABLE_NAME][colName][value]) == 0:
                    session[self.TABLE_MAP.TABLE_NAME][colName].pop(value)

    def doesSearchColumnExistInTable(self, columnName: str) -> bool:
        return columnName in session[self.TABLE_MAP.TABLE_NAME]
            
    def createListIfValueDoesNotExist(self, columnName: str, value: str) -> None:
        if value not in session[self.TABLE_MAP.TABLE_NAME][columnName]:
            session[self.TABLE_MAP.TABLE_NAME][columnName][value] = []

    def deleteRelatedEntities(self, childEntities: list[Self]|None = None)-> None:
        if (not childEntities):
            return None
        
        for childEntity in childEntities:
            childEntity.delete()

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
    def fromDict(self, row: dict)-> Self:
        ...

    @classmethod
    @abstractmethod
    def toDict(self)-> dict:
        ...


    