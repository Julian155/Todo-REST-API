from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Modules.Todo.Repository.Persistence.Query.TodoListQuery import TodoListQuery
from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity
from Shared.Todo.Transfer.TodoListCollectionTransfer import TodoListCollectionTransfer
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer

class TodoListRepository():
    def __init__(self, todoMapper: TodoMapper):
        self.todoMapper = todoMapper    

    def getTodoListTransferById(self, todoListId: str) -> TodoListTransfer|None:
        todoListEntity = self.getTodoListById(todoListId)

        if todoListEntity:
            return self.todoMapper.mapTodoListEntityToTransfer(todoListEntity)

        return None

    def getTodoListById(self, todoListId: str) -> TodoListEntity|None:
        return (TodoListQuery()
                    .useTodoEntryQuery()
                    .endUse()
                    .findOneByListId(todoListId))

    def getTodoListCollectionTransfer(self) -> TodoListCollectionTransfer:
        todoListEntities = self.getAllTodoLists()
 
        if todoListEntities:
            return self.todoMapper.mapTodoListEntitiesToCollectionTransfer(todoListEntities)

        return TodoListCollectionTransfer()
    
    def getAllTodoLists(self) -> list[TodoListEntity]|None:
        return (TodoListQuery()
                    .useTodoEntryQuery()
                    .endUse()
                    .find())

    def createTodoList(self, todoListData: dict)-> TodoListTransfer:
        todoListTransfer = TodoListTransfer()
        todoListTransfer.fromDict(todoListData)

        return todoListTransfer

    def updateTodoList(self, todoListId: str, todoListData: str) -> dict|None:
        todoListEntity = self.getTodoListById(todoListId)
        
        if todoListEntity:
            todoListEntity.setName(todoListData[TodoListTransfer.NAME])

            return {
                TodoListTransfer.ID: todoListId,
                TodoListTransfer.NAME: todoListEntity.getName()
            }

        return None

    def doesTodoListExist(self, todoListId: str)-> bool:
        todoListEntity = self.getTodoListById(todoListId)
        
        if todoListEntity:
            return True

        return False