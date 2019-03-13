from handler_mini_pattern import Handler_Mini_Pattern
from model import Pattern


class Handler_Pattern(Handler_Mini_Pattern):
    """
        Handles actions related to a Pattern object.
    """
    def get_yarn_list(self, suggested_yarn_list):
        """
            Returns yarn dictionary with name and weight.
        """

        yarn_list = []

        if len(suggested_yarn_list) > 0:
            if suggested_yarn_list[0].get('yarn_name'):
                for yarn in suggested_yarn_list:
                    yarn_name = yarn['yarn_name']
                    if yarn['yarn_weight'] is None:
                        yarn_weight = ''
                    else:
                        yarn_weight = yarn['yarn_weight']['name']

                    yarn_list.append({"yarn_weight" : yarn_name, "yarn_name" : yarn_weight})    

            else:
                yarn_list.append({"yarn_weight" : '', "yarn_name" : ''})
        else:
            yarn_list.append({"yarn_weight" : '', "yarn_name" : ''})


        return yarn_list  


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

        if pattern_dict['pattern_author']:
            if pattern_dict['pattern_author']['name']:
                author = pattern_dict['pattern_author']['name']
            else:
                author = ''
        else:
            author = ''

        if pattern_dict['free']:
            is_free = pattern_dict['free']
        else:
            is_free = ''

        photos_list = pattern_dict['photos']
        if photos_list:
            if len(photos_list) >= 1:
                img_fullsize_url = photos_list[0]['medium2_url']
                img_small_url = photos_list[0]['small_url']
            else:
                img_fullsize_url = ''
                img_small_url = ''
        else:
            img_fullsize_url = ''
            img_small_url = ''


        if pattern_dict['pattern_type']:
            if pattern_dict['pattern_type']['clothing']:
                is_clothing = pattern_dict['pattern_type']['clothing']
            else:
                is_clothing = ''
            if pattern_dict['pattern_type']['name']:
                pattern_type = pattern_dict['pattern_type']['name']
            else:
                pattern_type = ''
        else:
            is_clothing = ''
            pattern_type = ''

        if pattern_dict['downloadable']:
            is_downloadable = True
        else:
            is_downloadable = False

        if pattern_dict['download_location']:
            if pattern_dict['download_location']['url']:
                url = pattern_dict['download_location']['url']
            else:
                url = ''
        else:
            url = ''

        if pattern_dict['yardage_description']:
            yardage_description = pattern_dict['yardage_description']
        else:
            yardage_description = ''

        if pattern_dict['yarn_weight_description']:
            yarn_weight_description = pattern_dict['yarn_weight_description']
        else:
            yarn_weight_description = ''

        if pattern_dict['gauge_description']:
            gauge_description = pattern_dict['gauge_description']
        else:
            gauge_description = ''

        if pattern_dict['sizes_available']:
            sizes_available = pattern_dict['sizes_available']
        else:
            sizes_available = ''

        if pattern_dict['notes']:
            notes = pattern_dict['notes']
        else:
            notes = ''

        if pattern_dict['created_at']:
            created_at = pattern_dict['created_at']
        else:
            created_at = ''

        if pattern_dict['packs']:
            suggested_yarn_list = self.get_yarn_list(pattern_dict['packs'])
        else:
            suggested_yarn_list = []

        if pattern_dict['pattern_needle_sizes']:
            suggested_needles_list = pattern_dict['pattern_needle_sizes']
        else:
            suggested_needles_list = []


        pattern_values = {
            "pattern_id" : pattern_id,
            "name" : name,
            "author" : author,
            "is_free" : is_free,
            "img_fullsize_url" : img_fullsize_url,
            "img_small_url" : img_small_url,
            "is_clothing" : is_clothing,
            "pattern_type" : pattern_type,
            "is_downloadable" : is_downloadable,
            "url" : url,
            "yardage_description" : yardage_description,
            "yarn_weight_description" : yarn_weight_description,
            "gauge_description" : gauge_description,
            "sizes_available" : sizes_available,
            "notes" : notes,
            "created_at" : created_at,
            "suggested_yarn_list" : suggested_yarn_list,
            "suggested_needles_list" : suggested_needles_list
        }


        return pattern_values


    def create_pattern(self, pattern_values):
        """
            Returns pattern object of specified type by using data from dictionary provided.
        """
        
        return Pattern(pattern_values)


    def create_pattern_list(self, patterns_dict):
        """
            Returns a list with pattern objects by using list with dictionaries provided.
        """

        patterns_dict_list = []
        patterns_list = []

        for key, value in patterns_dict.items():
            patterns_dict_list.append(value)

        for p_dict in patterns_dict_list:
            pattern_values = self.set_values(p_dict)
            pattern = self.create_pattern(pattern_values)
            patterns_list.append(pattern)

        return patterns_list


    def create_pattern_dict(self, pattern):
        """
            Returns pattern dictionary by using data from pattern object provided.
        """

        pattern_dict = Pattern.as_dict(pattern)

        return pattern_dict