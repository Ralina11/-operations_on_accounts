from datetime import date

import utils
from utils import *
import pytest


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679010338980&signature=rK6z51QR_6FxbPj9wJJnlFJEm4jjKMELRYPlhb-0bGk&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679010338980&signature=rK6z51QR_6FxbPj9wJJnlFJEm4jjKMELRYPlhb-0bGk&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: BAD 400"

def test_get_filtered_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679010338980&signature=rK6z51QR_6FxbPj9wJJnlFJEm4jjKMELRYPlhb-0bGk&downloadName=operations.json"
    data, info = get_data(url)
    data = get_filtered_data(data)
    for i in data:
        assert i["state"] == "EXECUTED"

def test_format_date():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1679010338980&signature=rK6z51QR_6FxbPj9wJJnlFJEm4jjKMELRYPlhb-0bGk&downloadName=operations.json"
    data, info = get_data(url)
    data = format_date(get_filtered_data(data))
    for i in data:
        dt = datetime.strptime(i["date"], "%d.%m.%Y")
        assert i["date"] == dt.strftime("%d.%m.%Y")

@pytest.fixture
def one_data():
    return [{"from": "Счет 33407225454123927865"}, {"from": "MasterCard 9175985085449563"}, {"from": "Visa Classic 7022985698476865"}]

@pytest.fixture
def to_data():
    return [{"to": "Счет 83889757415570699323"}, {"to": "Visa Platinum 6086997013848217"}, {"to": "Visa Gold 2684274847577419"}]


def test_refactoring_from(one_data):
    one_data = refactoring_from(one_data)
    assert one_data[0] == {'from': 'Счет  3340 72** **** 7865'}
    assert one_data[1] == {'from': 'MasterCard  9175 98** **** 9563'}
    assert one_data[2] == {'from': 'Visa Classic  7022 98** **** 6865'}


def test_refactoring_to(to_data):
    to_data = refactoring_to(to_data)
    assert to_data[0] == {'to': 'Счет  **8897'}
    assert to_data[1] == {'to': 'Visa Platinum  **8699'}
    assert to_data[2] == {'to': 'Visa Gold  **8427'}