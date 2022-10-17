from DestinyRepository import DestinyRepository
from Ddd import Ddd


class UserInterface:
    def __init__(self, destiny_repository: DestinyRepository) -> None:
        self.destiny_repository = destiny_repository

    def get_user_input(self) -> Ddd:
        result = input(
            "Inform DDD (valid '##' - 2 numbers) from any available location: ").split()
        return Ddd(int(result[0]))
    
    
    def get_location(self, ddd: Ddd) -> int:
        return self.destiny_repository.get_location(ddd)

    def get_interaction(self) -> bool:
        Ddd = self.get_user_input()

        if (self.destiny_repository.check_if_itens_exists(Ddd) == False):
            print("Invalid code!")
            return False
        
        print(f"Location of this DDD: {self.get_location(Ddd)}")
        return True

