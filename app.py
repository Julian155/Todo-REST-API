from flask import Flask, session
from Modules.Todo.Routes.TodoListRoutes import todoListBluePrint
from Modules.Todo.Routes.TodoEntryRoutes import todoEntryBluePrint
from Modules.Search.Routes.SearchRoutes import searchBluePrint

from Modules.Kernel.KernelFactory import KernelFactory
import AppConfig

app = Flask(__name__)

app.config.from_object(AppConfig)

app.register_blueprint(todoEntryBluePrint)
app.register_blueprint(todoListBluePrint)
app.register_blueprint(searchBluePrint)

@app.before_request
def buildSession() -> None:
    kernelFactory = KernelFactory()
    if kernelFactory.createSessionHandler().isSessionFileEmpty():
        kernelFactory.createSessionBuilder().initSessionStructure()
        
        return
    
    kernelFactory.createSessionHandler().readSessionFile()
        
@app.after_request
def saveSessionToFile(response):
    KernelFactory().createSessionHandler().saveSessionToFile()
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

    





    
