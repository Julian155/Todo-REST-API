from typing_extensions import Self
from uuid import uuid4

from Shared.Kernel.Transfer.AbstractTransfer import AbstractTransfer

class TodoEntryTransfer(AbstractTransfer):
    ID = 'id'
    NAME = 'name'
    DESCRIPTION = 'description'

    def __init__(self):
        self.id = ''
        self.name = ''
        self.description = ''

    def getId(self) -> str:
        """
        :return str
        """

        return self.id

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

    def setId(self, id: str) -> None:
        """
        :param str id

        :return None
        """

        self.id = id

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


    def fromDict(self, todoEntryData: dict) -> Self:
        """Method to create a TodoEntry object from dictonary data

        :param dict todoEntryData

        :return Self
        """

        for key, value in todoEntryData.items():
            match key:
                case self.ID:
                    self.setId(value)
                case self.NAME:
                    self.setName(value)
                case self.DESCRIPTION:
                    self.setDescription(value)

        return self
        
    def toDict(self)-> dict:
        """returns Transfer object as dictionary

        :return dict
        """

        return {
            self.ID: self.getId(),
            self.NAME: self.getName(),
            self.DESCRIPTION: self.getDescription(),
        }




 