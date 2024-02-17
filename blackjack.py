import random
class Casino:
    @staticmethod
    def formDeck(aceCardValue:int) -> tuple:
        return [i for i in (list(range(2,11))+[10,10,10,aceCardValue]) for _ in range(4)]
class Player:
    def __init__(self,name:str) -> None:
        self.__name = name
        self.__deck = []
        self.__balance = 50
    @property
    def Name(self) -> str:
        return self.__name
    @property
    def Balance(self) -> int:
        return self.__balance
    @Balance.setter
    def Balance(self,inputBal:int):
        self.__balance = inputBal