from typing_extensions import Self
from Shared.Kernel.Transfer.AbstractTransfer import AbstractTransfer
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer

class TodoEntryCollectionTransfer(AbstractTransfer):
    TODO_ENTRIES = 'entries'

    def __init__(self):
        self.todoEntries = []

    def getTodoEntries(self) -> list[TodoEntryTransfer]:
        """
        :return list
        """

        return self.todoEntries

    def addTodoEntry(self, todoEntryTransfer: TodoEntryTransfer) -> None:
        """
        :param TodoEntryTransfer todoEntryTransfer

        :return None
        """

        self.todoEntries.append(todoEntryTransfer)

    def setTodoEntries(self, todoEntryTransfers: list[TodoEntryTransfer])-> None:
        self.todoEntries = todoEntryTransfers
    
    def fromDict(self, todoEntryCollectionData: dict) -> Self:
        """Method to create a TodoEntryTransferCollection object from dictonary data

        :param dict todoListCollectionData

        :return Self
        """

        for key, value in todoEntryCollectionData.items():
            match key:
                case self.TODO_ENTRIES:
                    self.todoEntries = value

        return self

    def toDict(self):
        """returns Transfer object as dictionary

        :return dict
        """
        
        return {
            self.TODO_ENTRIES: self.addToCollection(self.getTodoEntries())
        }
    
