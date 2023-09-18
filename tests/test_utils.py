from project import utils


def test_get_date_formatting():
    assert utils.get_date_formatting([{"date": "2019-08-26T10:50:58.294041"}]) == ["26.08.2019"]


def test_getting_an_map():
    assert utils.getting_an_map([
      {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
          "amount": "31957.58",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705190",
        "to": "Счет 64686473678894779589"
      }]) == [['Maestro', '1596 83** **** 5190']]
    assert utils.getting_an_map([
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]) == [['Данных о карте нет']]
    assert utils.getting_an_map([
        {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
        }]) == [['Счет', '7510 68** **** **** 6952']]
    assert utils.getting_an_map([
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }]) == [['Visa', 'Classic', '6831 98** **** 7658']]


def test_getting_an_invoice():
    assert utils.getting_an_invoice([{"to": "Счет 72082042523231456215"}]) == [['Счет', '**6215']]
