from typing_extensions import Self
from Shared.Kernel.Transfer.AbstractTransfer import AbstractTransfer
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer

class TodoListTransfer(AbstractTransfer):
    ID = 'id'
    NAME = 'name'
    ENTRIES = 'entries'

    def __init__(self):
        self.id = ''
        self.name = ''
        self.entries = []

    def getId(self) -> str:
        """
        :return str
        """

        return self.id

    def getEntries(self) -> list:
        """
        :return list
        """

        return self.entries

    def getName(self) -> str:
        """
        :return str
        """

        return self.name

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

    def addEntry(self, todoEntryTransfer: TodoEntryTransfer) -> Self:
        """
        :param TodoEntryTransfer todoEntryTransfer

        :return Self
        """

        self.entries.append(todoEntryTransfer)

        return self
    
    def fromDict(self, todoListData: dict) -> Self:
        """Method to create a TodoEntry object from dictonary data

        :param dict todoListData

        :return Self
        """

        for key, value in todoListData.items():
            match key:
                case self.ID:
                    self.setId(value)
                case self.NAME:
                    self.setName(value)
                case self.ENTRIES:
                    self.addToCollection(value)

        return self

    def toDict(self):
        """returns Transfer object as dictionary

        :return dict
        """

        return {
            self.ID: self.getId(),
            self.NAME: self.getName(),
            self.ENTRIES: self.addToCollection(self.getEntries())
        }
    
