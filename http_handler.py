### HTTP requests are handled here. ###

import requests
import json

class HTTP_Handler():

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



    def submit_post(self, URL, dictToSend):
        """Returns response of external api as json."""

        try: 
            response = requests.post(URL, json=dictToSend)
            return response.json()
        except:
            return {"status" : "500" , "reason" : "Post unsuccessful."}


    def submit_get(self, URL):
        """Returns response of external api as json."""
        try: 
            response = requests.get(URL, auth=self.AUTH)
            return response.json()
        except:
            return {"status" : "500" , "reason" : "Post unsuccessful."}


    def compose_url(self, pre_url, m_url, s_url):
        middel_url = m_url
        prefix_url = pre_url
        suffix_url = s_url

        partial_url = '{}{}{}'.format(prefix_url, middel_url, suffix_url)

        url = '{}{}'.format(self.BASE_URL, partial_url)

        return url