from Destiny import Destiny
from Ddd import Ddd

class DestinyRepository:
    destiny_itens: Destiny = []

    def __init__(self) -> None:
        pass

    def set_destiny_item(self, destiny: Destiny) -> None:
        self.destiny_itens.append(destiny)
    
    def get_location(self, ddd: Ddd) -> str:
        for item in self.destiny_itens:
            if (ddd.code == item.code):
                return item.name

    def check_if_itens_exists(self, ddd: Ddd) -> bool:
        for item in self.destiny_itens:
            if (ddd.code == item.code):
                return True

        return False

    def __str__(self) -> str:
        formatText = "{0:<30}\n"
        destiny = formatText.format("List of Locations available\n")

        for item in self.destiny_itens:
            destiny += formatText.format(item.name)

        return destiny
