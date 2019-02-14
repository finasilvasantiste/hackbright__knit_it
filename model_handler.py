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