from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Modules.Todo.Repository.Persistence.Query.TodoListQuery import TodoListQuery
from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity
from Modules.Todo.Repository.TodoQueryContainer import TodoQueryContainer
from Shared.Todo.Transfer.TodoListCollectionTransfer import TodoListCollectionTransfer
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer
from Modules.Todo.Repository.Persistence.Query.TodoEntryQuery import TodoEntryQuery
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer
from Shared.Todo.Transfer.TodoEntryCollectionTransfer import TodoEntryCollectionTransfer

class TodoRepository():
    def __init__(self, todoMapper: TodoMapper):
        self.todoMapper = todoMapper    

    def getTodoListTransferById(self, todoListId: str) -> TodoListTransfer|None:

        todoListEntity = self.getTodoListById(todoListId)

        if todoListEntity:
            return self.todoMapper.mapTodoListEntityToTransfer(todoListEntity)

        return None

    def getTodoListById(self, todoListId: str) -> TodoListEntity|None:
        return (TodoQueryContainer()
                    .queryTodoListWithEntries()
                    .findOneByListId(todoListId))

    def getTodoListCollectionTransfer(self) -> TodoListCollectionTransfer:
        todoListEntities = (TodoQueryContainer()
                                .queryTodoListWithEntries()
                                .find())
 
        if todoListEntities:
            return self.todoMapper.mapTodoListEntitiesToCollectionTransfer(todoListEntities)

        return TodoListCollectionTransfer()

    def createTodoList(self, todoListData: dict) -> TodoListTransfer:
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

    def doesTodoListExist(self, todoListId: str) -> bool:
        todoListEntity = self.getTodoListById(todoListId)
        
        if todoListEntity:
            return True

        return False

    def getTodoEntryCollectionTransfer(self, todoListId: str) -> TodoEntryCollectionTransfer:
        todoEntries = (TodoEntryQuery()
                        .findByFkTodoList(todoListId))

        if todoEntries:
            return self.todoMapper.mapTodoEntryEntitiesToCollectionTransfer(todoEntries)

        return TodoEntryCollectionTransfer()
    
    def getTodoEntryById(self, todoEntryId: str) -> TodoEntryEntity|None:
        return (TodoEntryQuery()
                .findOneByEntryId(todoEntryId))

    def createTodoEntryTransfer(self, todoEntryData: dict)-> TodoEntryTransfer:
        todoEntryTransfer = TodoEntryTransfer()
        todoEntryTransfer.fromDict(todoEntryData)

        return todoEntryTransfer