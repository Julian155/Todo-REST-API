from abc import ABC
from copy import deepcopy
from flask import session
from Modules.Kernel.Repository.Persistence.AbstractEntity import AbstractEntity
from typing_extensions import Self

class AbstractQuery(ABC):
    def __init__(self, entity: AbstractEntity, parentQuery: Self|None = None):
        self.entity = entity
        self.tableName = entity.TABLE_MAP.TABLE_NAME
        self.parentQuery = parentQuery
        self.filters = {}
        self.parentQueries = {}
        self.parentEntityCollection = {}
        self.childQueries = {}
        self.childEntityCollection = {}

    def findOneBy(self, column: str, value: int|str|bool) -> AbstractEntity|None:         
        row = session[self.tableName][column].get(value, None)

        return self.mapRowToEntity(row)
    
    def findRelatedEntities(self, parentId: str)-> None:
        if self.childQueries:
            query: AbstractQuery
            for tableName, query in self.childQueries.items():
                childEntities = query.findBy(tableName, parentId)

                self.childEntityCollection[tableName] = childEntities
                
    def findBy(self, column: str, value: int|str|bool) -> list|None:
        collection = []

        ids = session[self.tableName][column].get(value, None)
        if not ids: 
            return None

        for id in ids:
            entity = self.findOneBy('entity', id)
            collection.append(entity)

        return collection

    def findAll(self)-> list[Self]:
        collection = []

        rows: dict
        rows = session[self.tableName]['entity']
        
        if len(rows) == 0:
            return []

        for row in rows.values():
        
            entity = self.mapRowToEntity(row)
            collection.append(entity)
        
        return collection

    def mapRowToEntity(self, row: dict|None)-> AbstractEntity|None:  
        if row:
            self.entity.fromDict(row)
            self.entity.setNew(False)

            self.findRelatedEntities(self.entity.getId())
            self.mergeRelatedEntities()

            return deepcopy(self.entity)

        return None 

    def mergeRelatedEntities(self)-> None:
        return

    def endUse(self)-> Self:
        if not self.parentQuery:
            return self
        
        return self.parentQuery

    