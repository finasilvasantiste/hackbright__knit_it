### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler
from model_handler import Model_Handler

class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()
    MODEL_HANDLER = Model_Handler()

    def submit_request(self, b, a, q):
        """
            Submits request to HTTP Handler object.
        """
        base = b
        action = a
        query = q

        url = self.HTTP_HANDLER.compose_url(base, action , query)

        return self.HTTP_HANDLER.submit_get(url)


    def get_pattern_by_id(self, p_id):
        """
            Returns pattern by given id.
        """
        base = 'patterns/'
        action = p_id
        query = '.json'

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server


    def get_patterns_by_ids(self, ids_l):
        """
            Returns multiple patterns given a list of pattern ids.
        """
        base = 'patterns.json'
        ids_list = ids_l
        ids_string = ''

        for i in ids_list:
            ids_string = '{}+{}'.format(ids_string, i)

        base = 'patterns.json'
        action = '?ids='
        query = ids_string

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server


    def get_patterns(self):
        """
            Returns all patterns, 
            but only up to 100 at a time (provides paginator).
        """
        base = 'patterns/'
        action = 'search'
        query = '.json'

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server       


    def get_knitting_patterns(self):
        """
            Returns all knitting patterns, 
            but only up to 100 at a time (provides paginator).
        """
        base = 'patterns/'
        action = 'search'
        query = '.json?query=&craft=knitting'

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server  


    def get_knitting_patterns_by_page(self, p):
        """
            Returns all knitting patterns on a specific page.
        """
        page = p
        base = 'patterns/'
        action = 'search'
        query = '.json?query=&craft=knitting&page={}'.format(page)

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            # p_dict = resp_from_server['patterns'][0]
            # pattern = self.create_pattern(p_dict)

            pattern_dicts = resp_from_server['patterns']
            patterns = self.MODEL_HANDLER.create_pattern_list(pattern_dicts)
            patterns_dict = self.MODEL_HANDLER.create_pattern_dict_list(patterns)
            

            return patterns_dict  
