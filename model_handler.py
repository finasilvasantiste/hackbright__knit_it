### Requests that require usage of model classes are handled here. ###

from model import Pattern, Mini_Pattern

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


    def create_pattern_of_type(self, pattern_type, pattern_values):
        """
            Returns pattern object of specified type by using data from dictionary provided.
        """

        if pattern_type == 'mini pattern':
            return Mini_Pattern(pattern_values)
        elif pattern_type == 'pattern':
            return Pattern(pattern_values)