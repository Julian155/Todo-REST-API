from abc import ABC
from flask import session

class AbstractTableMap(ABC):
    TABLE_NAME = ''
    COL_PRIMARY = 'primary'
    
    RELATED_DELETION_TABLES = []
    RELATED_FK_TABLES = []
    CHILD_TABLE_COLUMN_NAMES = {}







        
