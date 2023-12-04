import requests


class ApiClient:
    """
    Class to work with Petstore API
    """
    _base_url = "https://petstore.swagger.io/v2"
    _pet_endpoint = "/pet"
    _store_endpoint = "/store"
    _inventory_endpoint = "/inventory"
    _order_endpoint = "/order"

    def add_pet(self, pet_data):
        """
        Add pet to the store
        :param pet_data: json with pet data
        """
        response = requests.post(f"{self._base_url}{self._pet_endpoint}", json=pet_data)
        return response

    def get_pet_by_id(self, pet_id):
        """
        Get pet by id
        :param pet_id: pet id (int)
        """
        response = requests.get(f"{self._base_url}{self._pet_endpoint}/{pet_id}")
        return response

    def delete_pet(self, pet_id):
        """
        Delete pet by id
        :param pet_id: pet id (int)
        """
        response = requests.delete(f"{self._base_url}{self._pet_endpoint}/{pet_id}")
        return response

    def get_pet_by_status(self, status):
        """
        Get pet by status
        :param status: pet status (str)
        """
        response = requests.get(f"{self._base_url}{self._pet_endpoint}/findByStatus?status={status}")
        return response

    def update_pet(self, pet_data):
        """
        Update pet by id
        :param pet_data: json with pet data (id is required)
        """
        response = requests.put(f"{self._base_url}{self._pet_endpoint}", json=pet_data)
        return response

    def get_inventory(self):
        """
        Get inventory
        """
        response = requests.get(f"{self._base_url}{self._store_endpoint}{self._inventory_endpoint}")
        return response

    def get_order_by_id(self, order_id):
        """
        Get order by id
        :param order_id: order id (int)
        """
        response = requests.get(f"{self._base_url}{self._store_endpoint}{self._order_endpoint}/{order_id}")
        return response

    def delete_order(self, order_id):
        """
        Delete order by id
        :param order_id: order id (int)
        """
        response = requests.delete(f"{self._base_url}{self._store_endpoint}{self._order_endpoint}/{order_id}")
        return response

    def add_order(self, order_data):
        """
        Add order to the store
        :param order_data: json with order data
        """
        response = requests.post(f"{self._base_url}{self._store_endpoint}{self._order_endpoint}", json=order_data)
        return response



