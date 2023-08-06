import datetime

import vlermv

class DatePrefixTransformer:
    '''
    Index must be a tuple of (date, string).
    '''
    def __init__(self, date_format):
        self.date_format = date_format

    def from_path(self, path):
        date_string, *rest = path
        return (datetime.datetime.strptime(date_string, self.date_format),) + tuple(rest)

    def to_path(self, index):
        date, *rest = index
        return (date.strftime(self.date_format),) + tuple(rest)

class DatePrefixVlermv(vlermv.S3Vlermv):
    serializer = vlermv.serializers.compressed_pickle

class Hour(DatePrefixVlermv):
    date_format = '%Y-%m-%d %H:00'
    transformer = DatePrefixTransformer(date_format)

class Day(DatePrefixVlermv):
    date_format = '%Y-%m-%d'
    transformer = DatePrefixTransformer(date_format)
