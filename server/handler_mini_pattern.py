from model import Mini_Pattern


class Handler_Mini_Pattern():
    """
        Handles actions related to a Mini Pattern object.
    """
    def create_pattern_dict_list(self, patterns_list):
        """
            Returns a list with pattern dictionaries by using list with pattern objects provided.
        """

        patterns_dict_list = []

        for p in patterns_list:
            p_dict = self.create_pattern_dict(p)
            patterns_dict_list.append(p_dict)


        return patterns_dict_list

    def create_pattern(self, pattern_values):
        """
            Returns pattern object of specified type by using data from dictionary provided.
        """
        return Mini_Pattern(pattern_values)

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
            img_small_url = pattern_dict['first_photo']['square_url']

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
            pattern = self.create_pattern(pattern_values)
            patterns_list.append(pattern)

        return patterns_list

    def create_pattern_dict(self, pattern):
        """
            Returns pattern dictionary by using data from pattern object provided.
        """
        pattern_dict = Mini_Pattern.as_dict(pattern)

        return pattern_dict