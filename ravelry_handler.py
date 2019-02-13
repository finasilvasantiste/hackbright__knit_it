### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler
from model import Pattern


class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()


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
            patterns = self.create_pattern_list(pattern_dicts)

            return resp_from_server  

    def create_pattern(self, p_dict):
        """
            Returns pattern object by using data from dictionary provided.
        """
        pattern_dict = p_dict

        pattern_id = pattern_dict['id']
        name = pattern_dict['name']
        is_free = pattern_dict['free']
        img_fullsize_url = pattern_dict['first_photo']['medium2_url']
        img_small_url = pattern_dict['first_photo']['small_url']
        
        pattern = Pattern(pattern_id, name, is_free, 
            img_fullsize_url, img_small_url)

        # print(pattern)

        return pattern


    def create_pattern_list(self, p_dict_list):
        """
            Returns a list with pattern objects by using list with dictionaries provided.
        """
        patterns_dict_list = p_dict_list
        patterns_list = []

        for p_dict in patterns_dict_list:
            pattern = self.create_pattern(p_dict)
            patterns_list.append(pattern)

            print(pattern)
            print('   ')

        print(len(patterns_list))

        return patterns_list