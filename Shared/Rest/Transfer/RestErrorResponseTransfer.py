from this import d
from typing_extensions import Self
from Shared.Rest.Transfer.AbstractRestResponseTransfer import AbstractRestResponseTransfer

class RestErrorResponseTransfer(AbstractRestResponseTransfer):
    ERROR_CODE = 'errorCode'
    MESSAGE = 'message'
    DESCRIPTION = 'description'

    errorCode = 0
    message = ''
    description = ''

    def getErrorCode(self) -> int:
        """
        :return int
        """

        return self.errorCode

    def getMessage(self) -> str:
        """
        :return str
        """

        return self.message

    def getDescription(self) -> str:
        """
        :return str
        """

        return self.description


    def setErrorCode(self, errorCode: int) -> Self:
        """
        :param int errorCode

        :return Self
        """

        self.errorCode = errorCode

        return self

    def setMessage(self, message: str) -> Self:
        """
        :param str message

        :return Self
        """

        self.message = message

        return self

    def setDescription(self, description: str) -> Self:
        """
        :param str description

        :return Self
        """

        self.description = description

        return self

    def toDict(self)-> dict:
        """returns Transfer object as dictionary

        :return dict
        """

        return {
            self.ERROR_CODE: self.errorCode,
            self.MESSAGE: self.message,
            self.DESCRIPTION: self.description,
        }
    
