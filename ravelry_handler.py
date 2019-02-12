### Calls to Ravelry Api are handled here. ###

from http_handler import HTTP_Handler


class Ravelry_handler():

    HTTP_HANDLER = HTTP_Handler()



    def get_pattern(self, p_id):
        
        url = self.HTTP_HANDLER.compose_url('patterns/', p_id)

        resp_from_server = self.HTTP_HANDLER.submit_get(url)

        return resp_from_server
    