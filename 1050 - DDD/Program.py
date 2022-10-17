from Destiny import Destiny
from DestinyRepository import DestinyRepository
from UserInterface import UserInterface

destiny_repository = DestinyRepository()
destiny_repository.set_menu_item(Destiny(61, "Brasília"))
destiny_repository.set_menu_item(Destiny(71, "Salvador"))
destiny_repository.set_menu_item(Destiny(11, "São Paulo"))
destiny_repository.set_menu_item(Destiny(21, "Rio de Janeiro"))
destiny_repository.set_menu_item(Destiny(32, "Juiz de Fora"))
destiny_repository.set_menu_item(Destiny(19, "Campinas"))
destiny_repository.set_menu_item(Destiny(27, "Vitoria"))
destiny_repository.set_menu_item(Destiny(31, "Belo Horizonte"))


print(destiny_repository)

user_interface = UserInterface(destiny_repository)

while user_interface.get_interaction():
    pass
