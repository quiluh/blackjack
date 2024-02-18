from random import choice

class Casino:
    deck = [i for i in (list(range(2,11))+[10,10,10,11]) for _ in range(4)]

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

    def hit(self) -> tuple:
        self.__deck.append(Casino.deck.pop(choice(Casino.deck)))
        return (self.__deck[-1],sum(self.__deck))
    
    def stand(self) -> int:
        return sum(self.__deck)
    
def playRound(player:Player,dealer:Player):

player = Player(input("Input Username: "))
dealer = Player("Dealer")

while player.Balance > 0:
    playRound(player,dealer)