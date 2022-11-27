from ._utils import UTILS

utils_datetime = UTILS()

class VARIABLES:
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SECRET_KEY = "<YOUR: SECRET_KEY>"
    SUFFIX_FILENAME = "{}_{}_{}_{}".format(utils_datetime.HOUR, 
    utils_datetime.MINUTE, utils_datetime.SECOND, utils_datetime.DAY)