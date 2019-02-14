### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler
from model_handler_search_requests import Model_Handler_Search_Requests
from model_handler_id_requests import Model_Handler_ID_Requests


class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()
    MODEL_HANDLER_SEARCH_REQUESTS = Model_Handler_Search_Requests()
    MODEL_HANDLER_ID_REQUESTS = Model_Handler_ID_Requests()

    def get_api_result(self, b, a, q):
        """
            Returns result from http request to external api.
        """
        base = b
        action = a
        query = q

        url = self.HTTP_HANDLER.compose_url(base, action , query)

        return self.HTTP_HANDLER.get_api_result(url)


    def get_patterns_by_ids(self, ids_l):
        """
            Returns patterns given a list of pattern ids.
        """
        base = 'patterns.json'
        ids_list = ids_l
        ids_string = ''

        for i in ids_list:
            ids_string = '{}+{}'.format(ids_string, i)

        base = 'patterns.json'
        action = '?ids='
        query = ids_string

        resp_from_server = self.get_api_result(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            pattern_dicts = resp_from_server['patterns']
            # patterns = self.MODEL_HANDLER.create_pattern_list(pattern_dicts)

            # print(patterns)
            return resp_from_server


    def get_patterns(self):
        """
            Returns all patterns, 
            but only up to 100 at a time (provides paginator).
        """
        base = 'patterns/'
        action = 'search'
        query = '.json'

        resp_from_server = self.get_api_result(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            pattern_dicts = resp_from_server['patterns']
            patterns = self.MODEL_HANDLER_SEARCH_REQUESTS.create_pattern_list(pattern_dicts)
            patterns_dict = self.MODEL_HANDLER_SEARCH_REQUESTS.create_pattern_dict_list(patterns)
            

            return patterns_dict      


    def get_knitting_patterns(self):
        """
            Returns all knitting patterns, 
            but only up to 100 at a time (provides paginator).
        """
        base = 'patterns/'
        action = 'search'
        query = '.json?query=&craft=knitting'

        resp_from_server = self.get_api_result(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            pattern_dicts = resp_from_server['patterns']
            patterns = self.MODEL_HANDLER_SEARCH_REQUESTS.create_pattern_list(pattern_dicts)
            patterns_dict = self.MODEL_HANDLER_SEARCH_REQUESTS.create_pattern_dict_list(patterns)
            

            return patterns_dict
            # return resp_from_server  


    def get_knitting_patterns_by_page(self, p):
        """
            Returns all knitting patterns on a specific page.
        """
        page = p
        base = 'patterns/'
        action = 'search'
        query = '.json?query=&craft=knitting&page={}'.format(page)

        resp_from_server = self.get_api_result(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            pattern_dicts = resp_from_server['patterns']
            patterns = self.MODEL_HANDLER_SEARCH_REQUESTS.create_pattern_list(pattern_dicts)
            patterns_dict = self.MODEL_HANDLER_SEARCH_REQUESTS.create_pattern_dict_list(patterns)
            

            return patterns_dict  
