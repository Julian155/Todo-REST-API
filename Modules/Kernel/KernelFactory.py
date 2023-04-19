from Modules.Kernel.Repository.DatabaseBuilder.SessionBuilder import SessionBuilder

class KernelFactory():
    def createSessionBuilder(self) -> SessionBuilder:
        
        return SessionBuilder()

