"""""
    ..module: Config.global.pyx
    This file should hold values
    that are used by the entire app,
    independent of framework used
"""
import os
from pyjtmorrisbytes.config.helpers import ConfigItem

# try getting all the information from the app first,
# otherwise fall back to defaults

class GlobalConfig(object):
    APP_NAME = ConfigItem("app")
    APP_AUTHOR = ConfigItem("Jordan Morris jthecybertinkerer@gmail.com")
    APP_TITLE = ConfigItem( str(APP_NAME) + " by " + str(APP_AUTHOR))
    #APP_AUTHOR_EMAIL = ConfigItem(__email__)
    APP_LISCENSE = ConfigItem("MIT")
    APP_URL = ConfigItem("https://www.jtmorrisbytes.com/")
    APP_SRC_URL = ConfigItem("http://www.github.com/" + str(APP_NAME))
    APP_ROOT_PATH = ConfigItem(os.path.join(os.path.abspath('.'), str(APP_NAME)))