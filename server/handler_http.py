### HTTP requests are handled here. ###

import requests
import json


class Handler_HTTP():

    BASE_URL = 'https://api.ravelry.com/'
    AUTH = ''

    def set_auth(self):
        with open('config.json', 'r') as f:
            config = json.load(f)

        USER = config['DEFAULT']['USER_NAME']
        PASSWORD = config['DEFAULT']['PASSWORD']
        self.AUTH = (USER, PASSWORD)


    def __init__(self):
        self.set_auth()


    def send_get_request(self, url, params):
        """Returns response of external api as json."""

        url = '{}{}'.format(self.BASE_URL, url)

        try:
            response = requests.get(url, auth=self.AUTH, params=params,)
            return response.json()
        except:
            return {"status" : "500" , "reason" : "Get unsuccessful."}
