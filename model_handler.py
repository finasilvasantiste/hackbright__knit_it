### Usage of model classes is handled here. ###

from model import Pattern

class Model_Handler():
    
    def create_pattern(self, p_dict):
        """
            Returns pattern object by using data from dictionary provided.
        """
        pattern_dict = p_dict

        pattern_id = pattern_dict['id']
        name = pattern_dict['name']
        is_free = pattern_dict['free']
        img_fullsize_url = pattern_dict['first_photo']['medium2_url']
        img_small_url = pattern_dict['first_photo']['small_url']
        
        pattern = Pattern(pattern_id, name, is_free, 
            img_fullsize_url, img_small_url)

        # print(pattern)

        return pattern


    def create_pattern_list(self, p_dict_list):
        """
            Returns a list with pattern objects by using list with dictionaries provided.
        """
        patterns_dict_list = p_dict_list
        patterns_list = []

        for p_dict in patterns_dict_list:
            pattern = self.create_pattern(p_dict)
            patterns_list.append(pattern)

            print(pattern)
            print('   ')

        print(len(patterns_list))

        return patterns_list


    def create_pattern_dict(self, p):
        """
            Returns pattern dictionary by using data from pattern object provided.
        """
        pattern = p

        pattern_dict = Pattern.as_dict(pattern)

        return pattern_dict



    def create_pattern_dict_list(self, p_list):
        """
            Returns a list with pattern dictionaries by using list with pattern objects provided.
        """

        patterns_list = p_list
        patterns_dict_list = []

        for p in patterns_list:
            p_dict = self.create_pattern_dict(p)
            patterns_dict_list.append(p_dict)


        return patterns_dict_list
