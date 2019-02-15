### Data Model is defined here. ###



class Mini_Pattern():
    

    def __init__(self, pattern_values):

        self.pattern_id = pattern_values['pattern_id']
        self.name = pattern_values['name']
        self.is_free = pattern_values['is_free']
        self.img_fullsize_url = pattern_values['img_fullsize_url']
        self.img_small_url = pattern_values['img_small_url']


    def __repr__(self):

        repr_s = "<Pattern pattern_id='{}' name='{}' is_free='{}' img_fullsize_url='{}' img_small_url='{}'>".format(
            self.pattern_id, self.name, self.is_free, self.img_fullsize_url, self.img_small_url)

        return repr_s

    @classmethod
    def as_dict(self, pattern):

        pattern_dict = {"pattern_id" : pattern.pattern_id, "name" : pattern.name, "is_free": pattern.is_free, "img_fullsize_ur": pattern.img_fullsize_url, "img_small_url": pattern.img_small_url}

        return pattern_dict

class Pattern(Mini_Pattern):

    def __init__(self, pattern_values):
        self.pattern_id = pattern_values['pattern_id']
        self.name = pattern_values['name']
        self.is_free = pattern_values['is_free']
        self.img_fullsize_url = pattern_values['img_fullsize_url']
        self.img_small_url = pattern_values['img_small_url']
        self.is_clothing = pattern_values['is_clothing']
        self.pattern_type = pattern_values['pattern_type']
        self.is_downloadable = pattern_values['is_downloadable']
        self.url = pattern_values['url']
        self.yardage = pattern_values['yardage']


    @classmethod
    def as_dict(self, pattern):

        pattern_dict = {
            "pattern_id" : pattern.pattern_id, 
            "name" : pattern.name, 
            "is_free": pattern.is_free, 
            "img_fullsize_ur": pattern.img_fullsize_url, 
            "img_small_url": pattern.img_small_url,
            "is_clothing" : pattern.is_clothing,
            "pattern_type" : pattern.pattern_type,
            "is_downloadable" : pattern.is_downloadable,
            "url" : pattern.url,
            "yardage" : pattern.yardage
            }

        return pattern_dict



class Needles():
    pass


class Yarn():
    pass


class Author():
    pass



### Associative Tables
class Pattern_Authors():
    pass


class Suggested_Yarn():
    pass


class Needles_Required():
    pass


