from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity
from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer

class TodoListEntityManager():
    def __init__(self, todoMapper: TodoMapper):
        self.todoMapper = todoMapper    

    def deleteTodoList(self, todoListEntity: TodoListEntity) -> None:
        todoListEntity.delete()
    
    def saveTodoList(self, todoListTransfer: TodoListTransfer) -> dict:
        todoListEntity = self.todoMapper.mapTodoListTransferToEntity(todoListTransfer)
        todoListEntity.save()

        todoListTransfer.setId(todoListEntity.getId())

        return todoListTransfer.toDict()

    def updateTodoList(self, todoListTransfer: TodoListTransfer, todoListEntity: TodoListEntity) -> None:
        todoListEntity = self.todoMapper.mapTodoListTransferToEntity(todoListTransfer, todoListEntity)

        todoListEntity.save()

        