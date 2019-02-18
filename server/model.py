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

        pattern_dict = {"pattern_id" : pattern.pattern_id, "name" : pattern.name, "is_free": pattern.is_free, "img_fullsize_url": pattern.img_fullsize_url, "img_small_url": pattern.img_small_url}

        return pattern_dict


class Pattern(Mini_Pattern):

    def __init__(self, pattern_values):
        self.pattern_id = pattern_values['pattern_id']
        self.name = pattern_values['name']
        self.author = pattern_values['author']
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

        self.suggested_yarn = Yarn.get_yarn_list(pattern_values['suggested_yarn_list'])
        self.suggested_needles = Needles.get_needles_list(pattern_values['suggested_needles_list'])

        # print(self)
        # print('+++++++++++')
        # print(pattern_values['suggested_needles_list'])


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

        repr_s = "<Pattern pattern_id='{}' name='{}' author='{}' is_free='{}' img_fullsize_url='{}' img_small_url='{}' is_clothing='{}' pattern_type='{}' is_downloadable='{}' url='{}' yardage='{}' yarn_weight='{}' gauge='{}' sizes='{}' description='{}' created_at='{}'".format(
            self.pattern_id, self.name, self.author, self.is_free, self.img_fullsize_url, 
            self.img_small_url, self.is_clothing, self.pattern_type, self.is_downloadable,
            self.url, self.yardage, self.yarn_weight, self.gauge, self.sizes, self.description, self.created_at)

        return repr_s


    @classmethod
    def as_dict(self, pattern):

        suggested_yarn_dict = Yarn.get_yarn_dicts(pattern.suggested_yarn)

        needles_dict = Needles.get_needles_dicts(pattern.suggested_needles)

        pattern_dict = {
            "pattern_id" : pattern.pattern_id, 
            "name" : pattern.name, 
            "author" : pattern.author,
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
            "created_at" : pattern.created_at,
            "suggested_yarn" : suggested_yarn_dict,
            "needles" : needles_dict
            }

        return pattern_dict



class Yarn():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    def __repr__(self):
        repr_s = "<Yarn name='{}' weight='{}'>".format(self.name, self.weight)
        return repr_s


    @classmethod
    def get_yarn_list(self, suggested_yarn_list):
        yarn_list = []

        for yarn in suggested_yarn_list:
            yarn_name = yarn['yarn_name']
            yarn_weight = yarn['yarn_weight']['name']

            yarn = Yarn(yarn_name, yarn_weight)

            yarn_list.append(yarn)

        return yarn_list


    @classmethod
    def get_yarn_dicts(self, yarn_list):
        yarn_dict_list = []

        for yarn in yarn_list:
            yarn_dict = Yarn.as_dict(yarn)

            yarn_dict_list.append(yarn_dict)

        return yarn_dict_list


    @classmethod
    def as_dict(self, yarn):

        yarn_dict ={
            "name" : yarn.name,
            "weight" : yarn.weight
        }

        return yarn_dict



class Needles():

    def __init__(self, name):
        self.name = name


    def __repr__(self):

        repr_s = "<Needles name='{}'>".format(self.name)

        return repr_s


    @classmethod
    def get_needles_list(self, suggested_needles_list):
        needles_list = []

        for needles in suggested_needles_list:
            needles_name = needles['name']

            needles = Needles(needles_name)

            needles_list.append(needles)

        return needles_list


    @classmethod
    def get_needles_dicts(self, needles_list):
        needles_dict_list = []

        for needles in needles_list:
            needles_dict = Needles.as_dict(needles)

            needles_dict_list.append(needles_dict)

        return needles_dict_list


    @classmethod
    def as_dict(self, needles):

        needles_dict ={
            "name" : needles.name
        }

        return needles_dict

