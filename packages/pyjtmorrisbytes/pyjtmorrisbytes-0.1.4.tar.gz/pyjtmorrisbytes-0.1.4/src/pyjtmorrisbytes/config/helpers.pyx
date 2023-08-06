import os
from importlib import import_module
import re
import json
from json.decoder import JSONDecodeError
from pyjtmorrisbytes import regex
import logging

logger = logging.getLogger(__name__)

class ConfigKey(object):
    name:str
    def __set_name__(self, owner, name):
        logger.debug("ConfigKey owner:", str(owner))
        try:
            logger.debug("ConfigKey owner name", str(owner.name))
        except:
            logger.debug("owner.name not found")
            pass
        try:
            logger.debug('ConigKey owner __name__', str(owner.__name__))
        except:
            pass
        logger.debug('ConfigKey incoming name:', str(name))
        self.name = name

class ConfigItem(object):
    value: object
    key:str
    default: object
    return_self:bool = False
    return_key: bool = False
    __name__:str = None
    def __init__(self, default=None, return_self=False, return_key=False):
        if return_key is True and return_self is True:
            raise ValueError("ConfigItem cannot be configured to return key"+ \
                             " and self at the at the same time.")
        self.default: type(default) = default
        self.value = default
        self.key = "default_value"
        self.return_self = return_self

    def __get__(self, instance, owner):
        if self.key:
            self.value = os.environ.get(self.key,self.default)
        else: 
            self.value = self.default
        if self.return_self:
            return self
        elif self.return_key:
            return self.key
        else:
            return self.value
    def __eq__(self, other):
        return self.value == other
    def __set_name__(self, owner, name):
        logger.debug(self)
        logger.debug(owner)
        logger.debug(name)
        self.__name__ = name
        self.key = name
    def __str__(self):
        return \
        "< " +self.__class__.__name__ + ": " + \
        "key: " + str(self.key) + ' value: ' + \
        str(self.value) + ' default: ' + str(self.default) + \
        '>'

def coerce(self, value, other, fallthrough_on_error=False, use_experimental=False):

    error = None
    # return_value
    coersion_error_msg = "Cannot coerce value " + str(value)
    coersion_error = ValueError(coersion_error_msg + ' to type '  + str(type(other)))
    logger.debug('coercing "', value,'of type:', type(value).__name__, "to type:", str(type(other)),
            'with value: ' + str(other))
    if isinstance(value, type(other)) or type(value) is type(other) or type(value) == type(other):
        return value
    elif isinstance(other, str) or other is str:
        return str(value)
#        elif not isinstance(other, str):
#            if type(value) = str:

        
    elif isinstance(value, str):
        logger.debug("coerce: found string, attempting conversion")
        if len(value) <= 0:
            logger.debug("coerce: found empty string,")
            if isinstance(other, dict):
                logger.debug('coerce: returning empty dictionary')
                return {}
            elif isinstance(other, list):
                logger.debug('coerce: returning empty list')
                return []
            elif isinstance(other, tuple):
                logger.debug('coerce: returning empty dictionary')
                return tuple()
            else:
                raise ValueError(coersion_error_msg + 'to ' + str(type(other))+ 
                "value was " + str(type(value)) + " and as empty")
        else:
            logger.debug("coerce: string is greater than zero, continuing")
            if isinstance(other, bool) or other is bool:
                logger.debug("coerce: requested conversion to bool")
                if value == '0' or value == '1' or \
                    value == 'True' or value == 'False':
                    logger.debug("coerce: returning boolean")
                    return bool(value)
                else:
                    raise coersion_error
            elif isinstance(other, int) or other is int:
                logger.debug("coerce: requested conversion to int")
                if re.match(regex.strict_optionally_signed_int, value) is not None:
                    logger.debug('coerce: matched integer, value=', value)
                    return int(value)
                else:
                    raise coersion_error
            elif isinstance(other, float) or other is float: 
                if re.match(regex.strict_optionally_signed_decimal, value) is not None:
                    return float(value)
                else:
                    logger.debug("coersion: converting string fell through")
                    raise coersion_error
            elif isinstance(other, dict) or other is dict:
                # I am still working on a regex to match this. for now,
                # I am blindly attempting to coerce a string to a dict.
                # If you try to coerce an invalid dictionary, you will
                # get a ValueError
                if use_experimental:
                    try:
                        return json.loads(value)
                    except json.decoder.JSONDecodeError as decodeError:
                        if fallthrough_on_error:
                            return value
                        else:
                            logger.debug("coerce: exception coercing string to dict")
                            logger.debug(decodeError)
                            raise coersion_error
                else:
                    if fallthrough_on_error:
                        return value
                    else:
                        raise NotImplementedError("Converting a string to a dict is not implemented yet")
            elif isinstance(other, list) or other is list:
                # In order to Coerce a string to a list, the string needs
                # to be corectly parsed and checked for double and single
                # quotes and is prone to errors, for now you should
                # make sure to triple check you data and turn on fallthrough
                # if you need to access the original value
                if fallthrough_on_error:
                    return value
                else:
                    raise NotImplementedError("Converting a string to a dict is not implemented yet")
            else:
                raise coersion_error
    elif isinstance(other, bool) or other is bool:
        if isinstance(value, int) or value is int:
            return int(value)
        elif isinstance(value, float) or value is float:
            return float(value)
    # elif isinstance(value, int):
    #     if isinstance(other, bool):
    #         return bool(value)
    #     elif isinstance(other, float):
    #         return float(value)
    #     else:
    #         raise coersion_error
    # elif isinstance(value, bool):
    #     return bool(value)
    # elif isinstance(other, float):
    #     return float(value)
    else:
        return value


# implementation notes:
# consider using **kwargs for the config object
def do_modular_import(module_name: str, import_name: str, members: list, top_level=True, use_defaults=False):

    gbl = globals()
    gbl[module_name] = import_module(module_name)
    for toImport in members:
        if not type(toImport) == tuple:
            raise ValueError("do_modular_import: expected a tuple in members, got: " + str(type(toImport))+
                             ' with value : ' + toImport)
        elif len(toImport) < 2 or len(toImport) > 2:
            raise Exception('do_modular_import: expected tuple with length 2, got ' + "")
        else:
            if top_level is True:
                module_to_import = toImport[0]
            elif import_name:
                module_to_import = import_module + "." + toImport[0]
            else:
                module_to_import = module_name + '.' + toImport[0]
            try:
                gbl[module_to_import] = import_module(module_name + '.' + toImport[0])
            except ImportError:
                if use_defaults:
                    gbl[module_to_import] = toImport[1]
