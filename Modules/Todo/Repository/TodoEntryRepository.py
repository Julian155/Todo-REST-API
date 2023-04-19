from Modules.Todo.Repository.Persistence.Query.TodoEntryQuery import TodoEntryQuery
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from Shared.Todo.Transfer.TodoEntryTransfer import TodoEntryTransfer
from Shared.Todo.Transfer.TodoListTransfer import TodoListTransfer

class TodoEntryRepository():
    def getTodoEntryById(self, todoEntryId: str) -> TodoEntryEntity|None:
        return TodoEntryQuery().findOneByEntryId(todoEntryId)

    def createTodoEntryTransfer(self, todoEntryData: dict)-> TodoEntryTransfer:
        todoEntryTransfer = TodoEntryTransfer()
        todoEntryTransfer.fromDict(todoEntryData)

        return todoEntryTransfer
