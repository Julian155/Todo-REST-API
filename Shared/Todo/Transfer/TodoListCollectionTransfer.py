from typing_extensions import Self
from Shared.Kernel.Transfer.AbstractTransfer import AbstractTransfer
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer

class TodoListCollectionTransfer(AbstractTransfer):
    TODO_LISTS = 'lists'

    def __init__(self):
        self.todoLists = []

    def getTodoLists(self) -> list[TodoListTransfer]:
        """
        :return list
        """

        return self.todoLists

    def addTodoList(self, todoListTransfer: TodoListTransfer) -> None:
        """
        :param TodoListTransfer todoListTransfer

        :return None
        """

        self.todoLists.append(todoListTransfer)

    def setTodoLists(self, todoListTransfers: list[TodoListTransfer])-> None:
        self.todoLists = todoListTransfers
    
    def fromDict(self, todoListData: dict) -> Self:
        """Method to create a TodoListTransferCollection object from dictonary data

        :param dict todoListCollectionData

        :return Self
        """

        for key, value in todoListData.items():
            match key:
                case self.TODO_LISTS:
                    self.todoLists = value

        return self

    def toDict(self):
        """returns Transfer object as dictionary

        :return dict
        """

        return {
            self.TODO_LISTS: self.addToCollection(self.getTodoLists())
        }
    
