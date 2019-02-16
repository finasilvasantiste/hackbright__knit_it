### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler
from model_handler_mini_patterns import Model_Handler_Mini_Pattern
from model_handler_patterns import Model_Handler_Pattern


class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()
    MODEL_HANDLER_MINI_PATTERNS = Model_Handler_Mini_Pattern()
    MODEL_HANDLER_PATTERNS = Model_Handler_Pattern()
    
    URL_RETURNS_MINI_PATTERNS = "patterns/search.json"
    URL_RETURNS_PATTERNS = "patterns.json"


    def get_api_result(self, url, params):
        """
            Returns result from http get request to external api.
        """
        return self.HTTP_HANDLER.send_get_request(url, params)


    def get_knitting_patterns_by_ids(self, ids_list):
        """
            Returns knitting patterns given a list of pattern ids.
        """
        ids_string = ''

        for i in ids_list:
            ids_string = '{}, {}'.format(ids_string, i)

        ids_string = ids_string[1:]    

        params = {
            "ids" : ids_string,
            "craft" : "knitting"
        }

        resp_from_server = self.get_api_result(self.URL_RETURNS_PATTERNS, params)


        if resp_from_server.get('status'):
            return resp_from_server
        else:
            patterns_dicts = self.get_patterns_dict(resp_from_server)

            return patterns_dicts
            # return resp_from_server 


    def get_patterns(self):
        """
            Returns all patterns, 
            but only up to 100 at a time (provides paginator).
        """

        params = {
            "query" : ""
        }

        resp_from_server = self.get_api_result(self.URL_RETURNS_MINI_PATTERNS, params)

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

        params = {
            "query" : "",
            "craft" : "knitting"
        }

        resp_from_server = self.get_api_result(self.URL_RETURNS_MINI_PATTERNS, params)

        if resp_from_server.get('status'):
            return resp_from_server
        else:
            patterns_dicts = self.get_mini_patterns_dict(resp_from_server)

            return patterns_dicts
            # return resp_from_server  


    def get_knitting_patterns_by_query(self, query, page_number=None):
        """
            Returns all knitting patterns matching search query,
            but only up to 100 at a time (provides paginator).
            Optional argument page number. 
        """

        query_list = query.split("+")
        query_string = ""

        if len(query_list) >1:
            for i in query_list:
                query_string = '{} {}'.format(query_string, i)
        else:
            query_string = query  

        if page_number:        
            params = {
                "query" : query_string,
                "craft" : "knitting",
                "page" : page_number
            }
        else:
            params = {
                "query" : query_string,
                "craft" : "knitting"
            }   
        

        # if page_number:
        #     resp_from_server = self.get_next_page(base, action, query, page_number)
        # else:
        #     resp_from_server = self.get_api_result(base, action, query)

        # if resp_from_server['paginator']['page'] != resp_from_server['paginator']['page_count']:
        #     ## TO-DO: Implement paginating
        #     print('Query result has {} pages.'.format(resp_from_server['paginator']['page_count']))

        resp_from_server = self.get_api_result(self.URL_RETURNS_MINI_PATTERNS, params)

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