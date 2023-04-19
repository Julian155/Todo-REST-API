from flask import Blueprint
from Modules.Todo.Controller.TodoEntryController import TodoEntryController

todoEntryBluePrint = Blueprint('TodoEntryRoutes', __name__)

todoEntryBluePrint.route('/todo-list/<string:todoListId>/entry', methods=['POST'])(TodoEntryController().addEntryToTodoList)
todoEntryBluePrint.route('/entry/<string:todoEntryId>', methods=['PATCH'])(TodoEntryController().updateTodoEntry)
todoEntryBluePrint.route('/entry/<string:todoEntryId>', methods=['DELETE'])(TodoEntryController().deleteTodoEntry)