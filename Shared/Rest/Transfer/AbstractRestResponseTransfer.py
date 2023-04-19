from typing_extensions import Self
from Shared.Kernel.Transfer.AbstractTransfer import AbstractTransfer

class AbstractRestResponseTransfer(AbstractTransfer):
    statusCode = 200

    def getStatusCode(self) -> int:
        """
        :return int
        """

        return self.statusCode

    def setStatusCode(self, statusCode: int) -> Self:
        """
        :param int statusCode

        :return Self
        """

        self.statusCode = statusCode

        return self
    
