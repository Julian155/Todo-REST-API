from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Modules.Todo.Repository.TodoListRepository import TodoListRepository
from Modules.Todo.Repository.TodoListEntityManager import TodoListEntityManager
from Modules.Todo.Repository.TodoEntryRepository import TodoEntryRepository
from Modules.Todo.Repository.TodoEntryEntityManager import TodoEntryEntityManager

class TodoFactory():
    def createTodoEntryEntityManager(self) -> TodoEntryEntityManager:
        
        return TodoEntryEntityManager(
            self.createTodoMapper()
        )

    def createTodoEntryRepository(self) -> TodoEntryRepository:

        return TodoEntryRepository()

    def createTodoListEntityManager(self) -> TodoListEntityManager:
        
        return TodoListEntityManager(
            self.createTodoMapper()
        )

    def createTodoListRepository(self) -> TodoListRepository:

        return TodoListRepository(
            self.createTodoMapper()
        )

    def createTodoMapper(self) -> TodoMapper:

        return TodoMapper()