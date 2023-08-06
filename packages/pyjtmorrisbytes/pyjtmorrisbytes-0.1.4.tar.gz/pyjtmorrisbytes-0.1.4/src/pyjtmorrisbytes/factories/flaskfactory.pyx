"""
    Name: flaskfactory.py
    Author: Jordan Morris

        This module is responsible for handling default configuration
    and creating application instances.

        The primary goal of this application factory is to handle
    configuration code and provide a way for dependants to access
    an application instance without having to create circular
    dependancies or rely on an init.py file.
        The secondary goal of this appliaction factory is to
    reduce the need to copy/paste or rewrite application
    configuration across all the applications that I make.
    I am hoping that I can write such a configuration that
    will allow me to import this code like a 'drop in' module
    and call create_app and the function would handle creating
    all the config defined in config files or environment
    variables.
        The third goal of this application factory class is to
    provide a common interface for the configuration files. I
    was hoping to use this class to help me generate config
    files if I deemed it to be a helpful and neccessary feature

"""



import cython
import os
from flask import Flask
from flask import Blueprint
from flask.config import Config
import re
import json
from json.decoder import JSONDecodeError
import datetime
from importlib import import_module
import types
from pyjtmorrisbytes.config.helpers import ConfigItem
from pyjtmorrisbytes.config.globalconf import GlobalConfig
# import dependancies from parent application
# this module expects your dependancies to 
# be defined inside a namespace called app.
#
# If the module cannot find what it is looking for,
# It attempts to load an equivalent default from 
# namespace pyjtmorrisbytes
#
# The module will be expecting the following tokens
# app.models (Database models)
# app.views (blueprints)

# do modular importing: try except for requested attributes
from pyjtmorrisbytes import models, views, controllers
try:
    from app import models, views, controllers
except:
    pass


# implementation notes:
#    Find an easy, expressive manner to construct a config object
#  from all these keys. It would be nice if my applications could
#  use an object like this to configure from code as well as access
#  defaults.
#
#    The primary purpose of this object is to provide a way to be
#  able to query the keys without having to remember them all. 
#  The secondary purpose of this object is to provide sane defaults
#  as fallbacks to querying environment variables
#
#    Maybe there could be a way to use this object to generate a
#  config file if none ws found?



def create_app(name: str, blueprints: list = None, root_path:str = '.', template_folder: str= 'templates',
                 static_folder: str= 'static', **kwargs):
    appinstance = Flask(name, 
                  template_folder=template_folder,
                  static_folder=static_folder,
                  root_path=root_path)
    if blueprints is not None and len(blueprints) > 0:
        for blueprint in blueprints:
            if isinstance(blueprint, Blueprint):
                appinstance.register_blueprint(blueprint)
            else:
                raise ValueError(
                    "create-app expects *args to be Blueprints," +
                    "got got type " + type(blueprint))
    else:
        raise ValueError("create-app: at least one blueprint is required," +
                         " got none or an empty list")
    if kwargs is not None:
        for key, value in kwargs.items():
            if isinstance(value, Blueprint):
                raise ValueError("create-app: A flask.Blueprint was found in **kwargs. " +
                                 "expected flask.Blueprints to be in *args.")
            elif isinstance(value, ConfigItem):
                try:
                    config_item_key = getattr(value, 'key')
                    config_item_value = getattr(value, 'value')
                except:
                    appinstance.config.update({key: value})
                else:
                    appinstance.config.update(
                        {config_item_key: config_item_value})
            else:
                appinstance.config.update({key: value})
                

    return appinstance


