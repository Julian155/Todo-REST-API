from Modules.Todo.Repository.Mapper.TodoMapper import TodoMapper
from Modules.Todo.Repository.TodoEntitiyManager import TodoEntityManager
from Modules.Todo.Repository.TodoRepository import TodoRepository

class TodoFactory():
    def createTodoRepository(self) -> TodoRepository:
        return TodoRepository(
            self.createTodoMapper()
        )

    def createTodoEntitiyManager(self) -> TodoEntityManager:

        return TodoEntityManager(
            self.createTodoMapper()
        )

    def createTodoMapper(self) -> TodoMapper:

        return TodoMapper()

