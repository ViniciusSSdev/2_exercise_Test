from Destiny import Destiny
from Ddd import Ddd
from DestinyRepository import DestinyRepository


def test_set_destiny_item():
    # Arrange
    destiny_repository = DestinyRepository()
    destiny_repository.Destiny_itens = []
    destiny1 = Destiny(1, "new york")
    destiny2 = Destiny(2, "cabuçu")
    destiny3 = Destiny(3, "Test 3")
    # Act

    destiny_repository.set_destiny_item(destiny1)
    destiny_repository.set_destiny_item(destiny2)

    # Assert
    assert len(destiny_repository.destiny_itens) == 2
    assert not destiny3 in destiny_repository.destiny_itens
    assert type(destiny_repository.destiny_itens) == list


def test_check_if_itens_exists():
    # Arrange
    destiny_repository = DestinyRepository()
    destiny_repository.destiny_itens = []
    destiny1 = Destiny(12, "Test 1")
    ddd1 = Ddd(12)
    ddd2 = Ddd(21)
    # Act

    destiny_repository.set_destiny_item(destiny1)
    resultNOK = destiny_repository.check_if_itens_exists(ddd1)
    resultOK = destiny_repository.check_if_itens_exists(ddd2)


    # Assert
    assert len(destiny_repository.destiny_itens) == 1
    assert resultNOK == True
    assert resultOK == False
