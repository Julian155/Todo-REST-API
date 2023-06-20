from Modules.Kernel.Repository.SessionBuilder.SessionBuilder import SessionBuilder
from Modules.Utils.SessionHandler import SessionHandler

class KernelFactory():
    def createSessionBuilder(self) -> SessionBuilder:
        
        return SessionBuilder()
    
    def createSessionHandler(self) -> SessionHandler:
        
        return SessionHandler()

