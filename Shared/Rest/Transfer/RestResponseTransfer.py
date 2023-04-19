from typing_extensions import Self
from Shared.Rest.Transfer.AbstractRestResponseTransfer import AbstractRestResponseTransfer

class RestResponseTransfer(AbstractRestResponseTransfer):
    responseData = {}

    def getResponseData(self) -> dict:
        """
        :return dict
        """

        return self.responseData


    def addResponseData(self, responseData: dict) -> Self:
        """
        :param str key
        :param dict responseData

        :return Self
        """

        self.responseData = self.responseData | responseData

        return self

    def toDict(self)-> dict:
        """returns Transfer object as dictionary

        :return dict
        """

        return self.responseData
    
