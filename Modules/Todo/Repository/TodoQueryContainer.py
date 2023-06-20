from Modules.Todo.Repository.Persistence.Query.TodoListQuery import TodoListQuery

class TodoQueryContainer():
    def queryTodoListWithEntries(self) -> TodoListQuery:
        return (TodoListQuery()
                .useTodoEntryQuery()
                .endUse())
        
        
