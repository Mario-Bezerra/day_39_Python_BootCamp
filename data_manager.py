from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "xxxx"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def update_price(self, id):
        from main import flight
        if flight.price>0:
            new_data = {
                    "price": {
                    "lowestPrice": flight.price
                    }
                }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{id}",
                json=new_data
                )
            print(response.text)
        else:
            new_data = {
                "price": {
                    "lowestPrice": 0
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{id}",
                json=new_data
            )
            print(response.text)

