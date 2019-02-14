### Search requests that require usage of model classes are handled here. ###

from model import Pattern
from model_handler import Model_Handler

class Model_Handler_Search_Requests(Model_Handler):

    def set_values(self, pattern_dict):
        """
            Returns pattern values by using data from dictionary provided.
        """

        pattern_id = pattern_dict['id']
        name = pattern_dict['name']
        is_free = pattern_dict['free']
        img_fullsize_url = pattern_dict['first_photo']['medium2_url']
        img_small_url = pattern_dict['first_photo']['small_url']

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

        pattern = Pattern(pattern_values["pattern_id"], pattern_values["name"], pattern_values["is_free"], 
            pattern_values["img_fullsize_url"], pattern_values["img_small_url"])

        return pattern


    def create_pattern_list(self, patterns_dict_list):
        """
            Returns a list with pattern objects by using list with dictionaries provided.
        """
        patterns_list = []

        for p_dict in patterns_dict_list:
            pattern_values = self.set_values(p_dict)
            pattern = self.create_pattern(pattern_values)
            patterns_list.append(pattern)

            print(pattern)
            print('   ')

        print(len(patterns_list))

        return patterns_list
