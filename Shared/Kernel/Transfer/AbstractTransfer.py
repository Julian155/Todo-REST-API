from typing_extensions import Self
from abc import ABC, abstractmethod

class AbstractTransfer(ABC):
    def addToCollection(self, values: list[Self]) -> list:
        valueList = []
        if not values:
            return valueList

        for value in values:
            valueList.append(value.toDict())

        return valueList

    @classmethod
    @abstractmethod
    def toDict(self, values: dict) -> dict:
        ...
