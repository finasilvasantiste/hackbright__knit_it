### Data Model is defined here. ###



class Pattern():
    
    def __init__(self, p_id, n, i_f, img_f_url, img_s_url):
        self.pattern_id = p_id
        self.name = n
        self.is_free = i_f
        self.img_fullsize_url = img_f_url
        self.img_small_url = img_s_url


    def __repr__(self):

        repr_s = "<Pattern pattern_id='{}' name='{}' is_free='{}' img_fullsize_url='{}' img_small_url='{}'>".format(
            self.pattern_id, self.name, self.is_free, self.img_fullsize_url, self.img_small_url)

        return repr_s



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


