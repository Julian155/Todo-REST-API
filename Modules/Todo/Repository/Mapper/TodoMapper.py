from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from Shared.Todo.Transfer.TodoEntryCollectionTransfer import TodoEntryCollectionTransfer
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer
from Shared.Todo.Transfer.TodoListCollectionTransfer import TodoListCollectionTransfer
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer
from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity

class TodoMapper():
    def mapTodoListTransferToEntity(self, todoListTransfer: TodoListTransfer, todoListEntity: TodoListEntity|None = None) -> TodoListEntity:
        todoListEntity = todoListEntity if todoListEntity else TodoListEntity()
        todoListEntity.fromDict(todoListTransfer.toDict())

        return todoListEntity

    def mapTodoListEntityToTransfer(self, todoListEntity: TodoListEntity, todoListTransfer: TodoListTransfer|None = None) -> TodoListTransfer:
        todoListTransfer = todoListTransfer if todoListTransfer else TodoListTransfer()
        todoListTransfer.fromDict(todoListEntity.toDict(False))

        if todoListEntity.getTodoEntryEntities():
            for todoEntryEntity in todoListEntity.getTodoEntryEntities():
                todoListTransfer.addEntry(self.mapTodoEntryEntityToTransfer(todoEntryEntity))

        return todoListTransfer

    def mapTodoEntryEntityToTransfer(self, todoEntryEntity: TodoEntryEntity, todoEntryTransfer: TodoEntryTransfer|None = None) -> TodoEntryTransfer:
        todoEntryTransfer = todoEntryTransfer if todoEntryTransfer else TodoEntryTransfer()
        todoEntryTransfer.fromDict(todoEntryEntity.toDict())

        return todoEntryTransfer 

    def mapTodoEntryTransferToEntity(self, todoEntryTransfer: TodoEntryTransfer, todoEntryEntity: TodoEntryEntity|None = None) -> TodoEntryEntity:
        todoEntryEntity = todoEntryEntity if todoEntryEntity else TodoEntryEntity()
        todoEntryEntity.setName(todoEntryTransfer.getName())
        todoEntryEntity.setDescription(todoEntryTransfer.getDescription())

        return todoEntryEntity

    def mapTodoListEntitiesToCollectionTransfer(self, todoListEntities: list[TodoListEntity]) -> TodoListCollectionTransfer:
        todoListCollectionTransfer = TodoListCollectionTransfer()

        for todoListEntity in todoListEntities:
            todoListCollectionTransfer.addTodoList(self.mapTodoListEntityToTransfer(todoListEntity))

        return todoListCollectionTransfer
    
    def mapTodoEntryEntitiesToCollectionTransfer(self, todoEntryEntities: list[TodoEntryEntity]) -> TodoEntryCollectionTransfer:
        todoEntryCollectionTransfer = TodoEntryCollectionTransfer()

        for todoEntryEntity in todoEntryEntities:
            todoEntryCollectionTransfer.addTodoEntry(self.mapTodoEntryEntityToTransfer(todoEntryEntity))

        return todoEntryCollectionTransfer