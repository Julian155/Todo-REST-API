from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer

class TodoEntryEntityManager():
    def __init__(self, todoMapper: TodoMapper):
        self.todoMapper = todoMapper    

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