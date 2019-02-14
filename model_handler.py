### Requests that require usage of model classes are handled here. ###

from model import Pattern

class Model_Handler():

    def create_pattern_dict(self, pattern):
        """
            Returns pattern dictionary by using data from pattern object provided.
        """

        pattern_dict = Pattern.as_dict(pattern)

        return pattern_dict


    def create_pattern_dict_list(self, patterns_list):
        """
            Returns a list with pattern dictionaries by using list with pattern objects provided.
        """

        patterns_dict_list = []

        for p in patterns_list:
            p_dict = self.create_pattern_dict(p)
            patterns_dict_list.append(p_dict)


        return patterns_dict_list
