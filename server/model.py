### Data Model is defined here. ###

import datetime
import pytz

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
        self.yardage = pattern_values['yardage_description']
        self.yarn_weight = pattern_values['yarn_weight_description']
        self.gauge = pattern_values['gauge_description']
        self.sizes = pattern_values['sizes_available']
        self.description = pattern_values['notes']
        self.created_at = self.convert_date_time(pattern_values['created_at'])

        print(self)


    def convert_date_time(self, date_time_str):
        """
            Converts date_time string to date_time object with UTC timezone.
        """ 
        date_time_list = date_time_str.split(" -") 
        print(date_time_list)
        date_time_str = date_time_list[0]
        print(date_time_str)

        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y/%m/%d %H:%M:%S')

        # print('Date:', date_time_obj.date())  
        # print('Time:', date_time_obj.time())  
        # print('Date-time:', date_time_obj) 

        utc_date_time = date_time_obj.astimezone(pytz.utc)

        return utc_date_time


    def __repr__(self):

        repr_s = "<Pattern pattern_id='{}' name='{}' is_free='{}' img_fullsize_url='{}' img_small_url='{}' is_clothing='{}' pattern_type='{}' is_downloadable='{}' url='{}' yardage='{}' yarn_weight='{}' gauge='{}' sizes='{}' description='{}' created_at='{}'".format(
            self.pattern_id, self.name, self.is_free, self.img_fullsize_url, 
            self.img_small_url, self.is_clothing, self.pattern_type, self.is_downloadable,
            self.url, self.yardage, self.yarn_weight, self.gauge, self.sizes, self.description, self.created_at)

        return repr_s


    @classmethod
    def as_dict(self, pattern):

        pattern_dict = {
            "pattern_id" : pattern.pattern_id, 
            "name" : pattern.name, 
            "is_free": pattern.is_free, 
            "img_fullsize_url": pattern.img_fullsize_url, 
            "img_small_url": pattern.img_small_url,
            "is_clothing" : pattern.is_clothing,
            "pattern_type" : pattern.pattern_type,
            "is_downloadable" : pattern.is_downloadable,
            "url" : pattern.url,
            "yardage" : pattern.yardage,
            "yarn_weight" : pattern.yarn_weight,
            "gauge" : pattern.gauge,
            "sizes" : pattern.sizes,
            "description" : pattern.description,
            "created_at" : pattern.created_at
            }

        return pattern_dict



class Needles():
    pass


class Yarn():
    pass


class Author():
    pass


