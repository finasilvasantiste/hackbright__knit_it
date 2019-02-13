### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler


class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()


    def get_pattern_by_id(self, p_id):
        
        url = self.HTTP_HANDLER.compose_url('patterns/', p_id , '.json')

        resp_from_server = self.HTTP_HANDLER.submit_get(url)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server

    def get_pattern_by_ids(self, ids_l):

        ids_list = ids_l
        ids_string = ''

        for i in ids_list:
            ids_string = '{}+{}'.format(ids_string, i)

        url = self.HTTP_HANDLER.compose_url('patterns.json', '?ids=' , ids_string)

        resp_from_server = self.HTTP_HANDLER.submit_get(url)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server



    def get_patterns(self):
        
        action = 'search'
        url = self.HTTP_HANDLER.compose_url('patterns/', action , '.json')

        resp_from_server = self.HTTP_HANDLER.submit_get(url)

        if resp_from_server.get('status'):
            return resp_from_server
        else:

            return resp_from_server            
    