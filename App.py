from flask import Flask, session
from Modules.Todo.Routes.TodoListRoutes import todoListBluePrint
from Modules.Todo.Routes.TodoEntryRoutes import todoEntryBluePrint
from Modules.Kernel.KernelFactory import KernelFactory
import AppConfig

app = Flask(__name__)

app.config.from_object(AppConfig)

app.register_blueprint(todoEntryBluePrint)
app.register_blueprint(todoListBluePrint)

@app.before_request
def buildSession():
    if not session.permanent: 
        KernelFactory().createSessionBuilder().initSessionStructure()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

    





    
