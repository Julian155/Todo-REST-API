from json import loads, dumps
from flask import session

class SessionHandler():
    def saveSessionToFile(self) -> None:
        self.clearSessionFile()
        
        with open('session.txt', 'w') as file: 
            file.write(dumps(dict(session)))
            
    def clearSessionFile(self) -> None:
        with open("session.txt", 'r+') as file:
            file.truncate(0)
            
    def readSessionFile(self) -> None:
        with open('session.txt') as file:
            sessionData  = file.read()
            
        if sessionData:
            session.update(loads(sessionData))
            
    def isSessionFileEmpty(self) -> bool:
        with open('session.txt') as file:
            sessionData = file.read()
            
        if sessionData:
            return False
        
        return True
