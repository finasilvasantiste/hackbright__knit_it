### Search requests that require usage of model classes are handled here. ###

from model import Mini_Pattern
from model_handler import Model_Handler

class Model_Handler_Mini_Pattern(Model_Handler):

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



    def create_pattern_list(self, patterns_dict_list):
        """
            Returns a list with mini pattern objects by using list with dictionaries provided.
        """
        patterns_list = []

        for p_dict in patterns_dict_list:
            pattern_values = self.set_values(p_dict)
            pattern = self.create_pattern_of_type('mini pattern', pattern_values)
            patterns_list.append(pattern)

            print(pattern)
            print('   ')

        print(len(patterns_list))

        return patterns_list