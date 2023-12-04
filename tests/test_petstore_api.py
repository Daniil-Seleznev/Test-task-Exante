from src.ApiClient import ApiClient

api_client = ApiClient()


class TestPet:

    def test_add_pet(self, pet_data):
        response = api_client.add_pet(pet_data)

        assert response.status_code == 200

    def test_get_pet_by_id(self, pet_data):
        api_client.add_pet(pet_data)
        pet_id = pet_data["id"]

        response = api_client.get_pet_by_id(pet_id)

        assert response.status_code == 200
        assert response.json()["name"] == pet_data["name"]

    def test_delete_pet(self, pet_data):
        api_client.add_pet(pet_data)
        pet_id = pet_data["id"]

        response = api_client.delete_pet(pet_id)
        assert response.status_code == 200

        response = api_client.get_pet_by_id(pet_id)
        assert response.status_code == 404

    def test_get_pet_by_status(self, pet_data):
        api_client.add_pet(pet_data)
        status = pet_data["status"]

        response = api_client.get_pet_by_status(status)

        assert response.status_code == 200
        assert pet_data["id"] in [pet["id"] for pet in response.json()]

    def test_update_pet(self, pet_data):
        api_client.add_pet(pet_data)
        pet_id = pet_data["id"]
        pet_data["name"] = "My Dog Name2"

        response = api_client.update_pet(pet_data)
        assert response.status_code == 200

        response = api_client.get_pet_by_id(pet_id)
        assert response.status_code == 200
        assert response.json()["name"] == pet_data["name"]


class TestStore:

    def test_get_inventory(self):
        response = api_client.get_inventory()

        assert response.status_code == 200

    def test_add_order(self, order_data):
        response = api_client.add_order(order_data)

        assert response.status_code == 200

    def test_get_order_by_id(self, order_data):
        api_client.add_order(order_data)
        order_id = order_data["id"]

        response = api_client.get_order_by_id(order_id)

        assert response.status_code == 200
        assert response.json()["id"] == order_data["id"]

    def test_delete_order(self, order_data):
        api_client.add_order(order_data)
        order_id = order_data["id"]

        response = api_client.delete_order(order_id)
        assert response.status_code == 200

        response = api_client.get_order_by_id(order_id)
        assert response.status_code == 404



