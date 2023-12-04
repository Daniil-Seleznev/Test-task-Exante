import pytest
from src.ApiClient import ApiClient


@pytest.fixture(scope="function")
def pet_data():
    """
    Fixture to return pet data to test and delete pet after test
    :return: pet data
    :rtype: dict
    """
    pet = {
        "id": 9888,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "My Dog Name",
        "photoUrls": ["https://example.com/buddy.jpg"],
        "tags": [
            {
                "id": 1,
                "name": "Friendly"
            }
        ],
        "status": "available"
    }

    yield pet
    api_client = ApiClient()
    api_client.delete_pet(pet["id"])


@pytest.fixture(scope="function")
def order_data():
    """
    Fixture to return order data to test and delete order after test
    :return: order data
    :rtype: dict
    """
    order = {
        "id": 9,
        "petId": 9888,
        "quantity": 1,
        "shipDate": "2021-04-28T18:47:31.123Z",
        "status": "placed",
        "complete": True
    }
    yield order
    api_client = ApiClient()
    api_client.delete_order(order["id"])

