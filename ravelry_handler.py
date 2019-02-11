### All calls to Ravelry Api are handled here. ###

import requests
import json

def Ravelry_Handler():

    BASE_URL = 'https://api.ravelry.com/'


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
            response = requests.get(URL)
            return response.json()
        except:
            return {"status" : "500" , "reason" : "Post unsuccessful."}


    def compose_url(self, pre_url, p_id):
        pattern_id = p_id
        prefix_url = pre_url
        suffix_url = '.json'

        partial_url = '{}{}{}'.format(prefix_url, pattern_id, suffix_url)

        url = '{}{}'.format(BASE_URL, partial_url)

        return url

    def get_pattern(self, p_id):
        
        url = self.compose_url('patterns/', p_id)

        resp_from_server = self.submit_get(url)

        return resp_from_server
    








