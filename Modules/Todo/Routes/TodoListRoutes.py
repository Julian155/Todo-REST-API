from flask import Blueprint
from Modules.Todo.Controller.TodoListController import TodoListController

todoListBluePrint = Blueprint('TodoListRoutes', __name__)

todoListBluePrint.route('/todo-list/<string:todoListId>', methods=['GET'])(TodoListController().getTodoListEntries)
todoListBluePrint.route('/todo-list/<string:todoListId>', methods=['DELETE'])(TodoListController().deleteTodoList)
todoListBluePrint.route('/todo-list/<string:todoListId>', methods=['PATCH'])(TodoListController().updateTodoList)
todoListBluePrint.route('/todo-list', methods=['POST'])(TodoListController().createTodoList)
todoListBluePrint.route('/todo-list', methods=['GET'])(TodoListController().getAllTodoLists)

