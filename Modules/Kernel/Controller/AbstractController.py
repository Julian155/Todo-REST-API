import json
from flask import Response
from Shared.Rest.Transfer.AbstractRestResponseTransfer import AbstractRestResponseTransfer
from abc import ABC

class AbstractController(ABC):
    def buildRespond(self, restResponseTransfer: AbstractRestResponseTransfer, headers = [])-> Response:
        """returns a new flask Response object

        :param AbstractRestResponseTransfer restResponseTransfer
        :param list headers

        :return Response
        """

        return Response(response=json.dumps(restResponseTransfer.toDict()), status=restResponseTransfer.getStatusCode(), headers=headers)