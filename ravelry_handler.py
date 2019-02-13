### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler


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
        base = 'patterns/'
        action = p_id
        query = '.json'

        resp_from_server = self.submit_request(base, action, query)


        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server


    def get_patterns_by_ids(self, ids_l):
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
        base = 'patterns/'
        action = 'search'
        query = '.json'

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server       


    def get_knitting_patterns(self):
        base = 'patterns/'
        action = 'search'
        query = '.json?query=&craft=knitting'

        resp_from_server = self.submit_request(base, action, query)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server  
    

