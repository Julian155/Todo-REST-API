from flask import render_template, redirect, url_for, request, abort, session, Response
from Modules.Kernel.Controller.AbstractController import AbstractController
from Shared.Rest.RestHttpCodes import RestHttpCodes
from Shared.Rest.Transfer.RestResponseTransfer import RestResponseTransfer
from Modules.Todo.TodoFactory import TodoFactory

class TodoListController(AbstractController):
    def getTodoList(self, todoListId: str):  
        todoListTransfer = TodoFactory().createTodoListRepository().getTodoListTransferById(todoListId)

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
                .addResponseData(todoListTransfer.getEntries())
            )
        )
        
    def getAllTodoLists(self):
        todoListCollectionTransfer = TodoFactory().createTodoListRepository().getTodoListCollectionTransfer()

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
                .addResponseData(todoListCollectionTransfer.toDict())
            )
        )

    def deleteTodoList(self, todoListId: str)-> Response:
        todoListEntity = TodoFactory().createTodoListRepository().getTodoListById(todoListId)

        if not todoListEntity:
            return '', 404
        
        TodoFactory().createTodoListEntityManager().deleteTodoList(todoListEntity)

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
            )
        )
    
    def createTodoList(self)-> Response:
        todoListData = request.form

        todoListTransfer = TodoFactory().createTodoListRepository().createTodoList(todoListData)

        todoList = TodoFactory().createTodoListEntityManager().saveTodoList(todoListTransfer)

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
                .addResponseData(todoList)
            )
        )

    def updateTodoList(self, todoListId: str)-> Response:
        todoListData = request.form

        todoListEntity = TodoFactory().createTodoListRepository().getTodoListById(todoListId)
        todoListTransfer = TodoFactory().createTodoListRepository().createTodoList(todoListData)

        TodoFactory().createTodoListEntityManager().updateTodoList(todoListTransfer, todoListEntity, todoListId)
        
        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
            )
        )
