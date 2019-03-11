import unittest
import handler_API
import handler_http
import json
from handler_pattern

class MockHandlerHttp(handler_http.Handler_HTTP):

    def __init__(self, mock_requests):
        self.mockSetup = mock_requests

    def send_get_request(self, url, params):
        """
        Urls parameter is usually static. Using params to differentiate between
        the requests

        :param url: target url
        :param params: list of parameters to call
        :return:
        """
        return self.mockSetup[json.dumps(params)]


class MockHandlerPatter(handler_pattern.Handler_Pattern):

    def __init__(self, mock_data):
        self.mockData = mock_data

    def create_pattern_list(self, patterns):
        return self.mockData[json.dumps(patterns[0])]


class TestHandler_API(unittest.TestCase):

    def test_get_knitting_patterns_by_ids(self):
        handler_api = handler_API.Handler_API()
        handler_api.HANDLER_HTTP = MockHandlerHttp({
            '{"ids": " 101, 102", "craft": "knitting"}':
                {'status': '500', 'reason': 'Get unsuccessful.'},
            '{"ids": " 103", "craft": "knitting"}':
                {'patterns': [ {'pattern': 'mockPattern'}] },

        })

        # test case 1: failure from downstream
        response = handler_api.get_knitting_patterns_by_ids([101, 102])
        self.assertEqual('500', response["status"])

        # test case 2: successful response
        response = handler_api.get_knitting_patterns_by_ids([103])

        



if __name__ == '__main__':
    unittest.main()




