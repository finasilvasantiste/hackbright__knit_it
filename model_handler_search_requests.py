### Search requests that require usage of model classes are handled here. ###

from model import Pattern
from model_handler import Model_Handler

class Model_Handler_Search_Requests(Model_Handler):

    def set_values(self, pattern_dict):
        """
            Returns pattern values by using data from dictionary provided.
        """

        if pattern_dict['id']:
            pattern_id = pattern_dict['id']
        else:
            pattern_id = ''

        if pattern_dict['name']:
            name = pattern_dict['name']
        else:
            name = ''

        if pattern_dict['free']:
            is_free = pattern_dict['free']
        else:
            is_free = ''

        if pattern_dict['first_photo']:
            img_fullsize_url = pattern_dict['first_photo']['medium2_url']
            img_small_url = pattern_dict['first_photo']['small_url']
        else:
            img_fullsize_url = ''
            img_small_url = ''


        pattern_values = {
            "pattern_id" : pattern_id,
            "name" : name,
            "is_free" : is_free,
            "img_fullsize_url" : img_fullsize_url,
            "img_small_url" : img_small_url
        }

        return pattern_values


    def create_pattern(self, pattern_values):
        """
            Returns pattern object by using data from dictionary provided.
        """


        # pattern = Pattern(pattern_values["pattern_id"], pattern_values["name"], pattern_values["is_free"], 
        #     pattern_values["img_fullsize_url"], pattern_values["img_small_url"])


        # return pattern

        return Pattern(pattern_values)
