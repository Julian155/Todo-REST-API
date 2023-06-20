from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity
from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer
from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer

class TodoEntityManager():
    def __init__(self, todoMapper: TodoMapper):
        self.todoMapper = todoMapper    

    def deleteTodoList(self, todoListEntity: TodoListEntity) -> None:
        todoListEntity.delete()
    
    def saveTodoList(self, todoListTransfer: TodoListTransfer) -> dict:
        todoListEntity = self.todoMapper.mapTodoListTransferToEntity(todoListTransfer)
        todoListEntity.save()

        todoListTransfer.setId(todoListEntity.getId())

        return todoListTransfer.toDict()

    def updateTodoList(self, todoListData: dict, todoListEntity: TodoListEntity) -> None:
        todoListEntity.setName(todoListData['name'])
        todoListEntity.save()

    def deleteTodoEntry(self, todoEntryEntity: TodoEntryEntity) -> None:
        todoEntryEntity.delete()

    def saveTodoEntry(self, todoEntryTransfer: TodoEntryTransfer, todoListId: str) -> dict:
        todoEntryEntity = self.todoMapper.mapTodoEntryTransferToEntity(todoEntryTransfer)
        todoEntryEntity.setFkTodoListId(todoListId)
        todoEntryEntity.save()

        todoEntryTransfer.setId(todoEntryEntity.getId())

        return todoEntryTransfer.toDict()

    def updateTodoEntry(self, todoEntryTransfer: TodoEntryTransfer, todoEntryEntity: TodoEntryEntity) -> None:
        todoEntryEntity = self.todoMapper.mapTodoEntryTransferToEntity(todoEntryTransfer, todoEntryEntity)
       
        todoEntryEntity.save()

        