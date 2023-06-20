from flask import Blueprint
from Modules.Search.Controller.SearchController import SearchController

searchBluePrint = Blueprint('SearchRoutes', __name__)

searchBluePrint.route('/todo-list/search', methods=['GET'])(SearchController().searchTodoLists)
searchBluePrint.route('/entry/search', methods=['GET'])(SearchController().searchEntries)
searchBluePrint.route('/search', methods=['GET'])(SearchController().searchAll)