### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler
from model_handler_mini_patterns import Model_Handler_Mini_Pattern
from model_handler_patterns import Model_Handler_Pattern


class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()
    MODEL_HANDLER_MINI_PATTERNS = Model_Handler_Mini_Pattern()
    MODEL_HANDLER_PATTERNS = Model_Handler_Pattern()

    def get_api_result(self, base, action, query):
        """
            Returns result from http request to external api.
        """

        url = self.HTTP_HANDLER.compose_url(base, action , query)

        return self.HTTP_HANDLER.submit_get(url)


    def get_patterns_by_ids(self, ids_list):
        """
            Returns patterns given a list of pattern ids.
        """
        base = 'patterns.json'
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

            patterns_dicts = self.get_patterns_dict(resp_from_server)

            return patterns_dicts


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
            patterns_dicts = self.get_mini_patterns_dict(resp_from_server)

            return patterns_dicts      


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
            patterns_dicts = self.get_mini_patterns_dict(resp_from_server)

            return patterns_dicts
            # return resp_from_server  


    def get_knitting_patterns_by_page(self, page):
        """
            Returns all knitting patterns on a specific page, 
            but only up to 100 at a time (provides paginator).
        """
        base = 'patterns/'
        action = 'search'
        query = '.json?query=&craft=knitting&page={}'.format(page)

        resp_from_server = self.get_api_result(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            patterns_dicts = self.get_mini_patterns_dict(resp_from_server)

            return patterns_dicts  


    def get_knitting_patterns_by_query(self, query, page_number=None):
        """
            Returns all knitting patterns matching search query. 
        """


        base = 'patterns/'
        action = 'search'
        query = '.json?query={}&craft=knitting'.format(query) 
        

        # if page_number:
        #     resp_from_server = self.get_next_page(base, action, query, page_number)
        # else:
        #     resp_from_server = self.get_api_result(base, action, query)

        # if resp_from_server['paginator']['page'] != resp_from_server['paginator']['page_count']:
        #     ## TO-DO: Implement paginating
        #     print('Query result has {} pages.'.format(resp_from_server['paginator']['page_count']))

        resp_from_server = self.get_api_result(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            patterns_dicts = self.get_mini_patterns_dict(resp_from_server)

            return patterns_dicts   



    # def get_next_page(self, base, action, query, page_number):
    #     """
    #         Returns next page of result.
    #     """
    #     page = 'page={}'.format(page_number)
    #     query = '{}&{}'.format(query, page)

    #     return self.get_api_result(base, action, query)



    def get_mini_patterns_dict(self, resp_from_server):
        """
            Returns list of mini patterns dictionaries using response from server provided.
        """

        patterns = self.MODEL_HANDLER_MINI_PATTERNS.create_pattern_list(resp_from_server['patterns'])
        patterns_dict = self.MODEL_HANDLER_MINI_PATTERNS.create_pattern_dict_list(patterns)
        
        return patterns_dict


    def get_patterns_dict(self, resp_from_server):
        """
            Returns list of patterns dictionaries using response from server provided.
        """

        patterns = self.MODEL_HANDLER_PATTERNS.create_pattern_list(resp_from_server['patterns'])
        patterns_dict = self.MODEL_HANDLER_PATTERNS.create_pattern_dict_list(patterns)
        
        return patterns_dict