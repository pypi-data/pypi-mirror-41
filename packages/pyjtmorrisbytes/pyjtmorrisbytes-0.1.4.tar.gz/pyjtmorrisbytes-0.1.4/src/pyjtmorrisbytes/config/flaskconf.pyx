from pyjtmorrisbytes.config.helpers import ConfigItem


from pyjtmorrisbytes.config.globalconf import GlobalConfig


import os
from datetime import timedelta
class DefaultConfig(GlobalConfig):
    def __init__(self):
        "noop"


    def __get__(self, instance, owner):
        print("DefaultConfig: called __get__")
        print("DefaultConfig instance", str(self))
        if instance:
            print("instance:" + str(instance))
        if owner:
            print("owner:" + str(owner))
    """
        ..class: config.flask.default
        "contains the key, value, default pairs for the default flask configuration"
    """
    FLASK_ENV = ConfigItem('production')
    """Tells flask what environment it is in. FLASK_ENV string: 'production', 'development'
        The following keys are set to True If FLASK_ENV=development:
        FLASK_DEBUG [attribute DEBUG]
        JSONIFY_PRETTY_PRINT
        EXPLAIN_TEMPLATE_RELOADING
        PRESERVE_CONTEXT_ON_EXCEPTION
        TRAP_BAD_REQUEST_ERRORS (if unset) 
    """
    FLASK_DEBUG: ConfigItem = ConfigItem(False)
    """ Turns on Flask DEBUG Mode. FLASK_DEBUG bool: True, False            
                                                                            
        FLASK_DEBUG [attribute DEBUG]                                       
                                                                            
        When FLASK_DEBUG is True, the following are also turned on by default

        JSONIFY_PRETTY_PRINT
        EXPLAIN_TEMPLATE_RELOADING
        PRESERVE_CONTEXT_ON_EXCEPTION
        TRAP_BAD_REQUEST_ERRORS (if unset)

        in addition, Auto reload will also be turned on when FLASK_DEBUG is True
    """
    TESTING = ConfigItem(False)
    """ Enables testing mode: Tells flask to reraise exceptions
        instead of catching them with the apps error handlers

        Turning on testing will enable the following:
        PROPAGATE_EXCEPTIONS    
    """
    PROPAGATE_EXCEPTIONS = ConfigItem(None)
    """ Tells flask to reraise exceptions instead of catching them with the app's error handlers"""

    # PRESERVE_CONTEXT_ON_EXCEPTION = 'PRESERVE_CONTEXT_ON_EXCEPTION'
    """Don’t pop the request context when an exception occurs"""
    TRAP_HTTP_EXCEPTIONS = ConfigItem(False)
    """ If there is no handler for an HTTPException-type exception,
        re-raise it to be handled by the interactive debugger instead 
        of returning it as a simple error response.
    """
    TRAP_BAD_REQUEST_ERRORS = ConfigItem('TRAP_BAD_REQUEST_ERRORS')
    SECRET_KEY = ConfigItem(os.urandom(32))
    SESSION_COOKIE_NAME = ConfigItem('jtmb-session')
    SESSION_COOKIE_DOMAIN = ConfigItem(None)
    SESSION_COOKIE_PATH = ConfigItem(None)
    SESSION_COOKIE_HTTPONLY = ConfigItem(True)
    SESSION_COOKIE_SECURE = ConfigItem(False)
    SESSION_COOKIE_SAMESITE = ConfigItem('Lax')
    PERMANENT_SESSION_LIFETIME = ConfigItem(timedelta(days=7))
    SESSION_REFRESH_EACH_REQUEST = ConfigItem(True)
    USE_X_SENDFILE = ConfigItem(False)
    SEND_FILE_MAX_AGE_DEFAULT = ConfigItem(timedelta(hours=24))
    SERVER_NAME = ConfigItem('localhost.dev')
    APPLICATION_ROOT = ConfigItem('/')
    USE_HTTPS = ConfigItem(False)
    if USE_HTTPS.value is True:
        PREFERRED_URL_SCHEME = ConfigItem('https')
    else:
        PREFERRED_URL_SCHEME = ConfigItem('http')
    MAX_CONTENT_LENGTH = ConfigItem(512000000)
    JSON_AS_ASCII = ConfigItem(True)
    JSON_SORT_KEYS = ConfigItem(True)
    JSONIFY_PRETTYPRINT_REGULAR = ConfigItem(True)
    JSONIFY_MIMETYPE = ConfigItem('application/json')
    TEMPLATES_AUTO_RELOAD = ConfigItem(True)
    EXPLAIN_TEMPLATE_LOADING = ConfigItem(False)
    MAX_COOKIE_SIZE = ConfigItem(4093)
    SQLALCHEMY_DATABASE_URI = ConfigItem('sqlite:///'+str(__class__.APP_NAME)+'.db')
    """the database url to be used when not on heroku"""

    core_interface_config_list= [
        ('ENV', 'development'),
        ('DEBUG', False), ('TESTING', False),
        # Flask Variables
        ('PROPOGATE_EXCEPTIONS', None),
        ('PRESERVE_CONTEXT_ON_EXCEPTION', None),
        ('TRAP_HTTP_EXCEPTIONS', False),
        ('TRAP_BAD_REQUEST_ERRORS', None),
        ('SECRET_KEY', os.urandom(32)), ('SESSION_COOKIE_NAME', 'jtmb-session'),
        ('SESSION_COOKIE_DOMAIN', None), ('SESSION_COOKIE_PATH', 'None'),
        ('SESSION_COOKIE_HTTPONLY', True), ('SESSION_COOKIE_SAMESITE', None),
        ('PERMANENT_SESSION_LIFETIME', timedelta(days=1)), 
        ('SESSION_REFRESH_EACH_REQUEST', True),
        ('USE_X_SENDFILE', False),
        ('SEND_FILE_MAX_AGE_DEFAULT', timedelta(hours=6)),
        ('SERVER_NAME', 'localhost.dev'), ('APPLICATION_ROOT', '/'),
        ('PREFERRED_URL_SCHEME', 'http'),
        ('MAX_CONTENT_LENGTH', 512000000), ('JOIN_AS_ASCII', True), ('JSON_SORT_KEYS', True),
        ('JSONIFY_PRETTYPRINT_REGULAR', False), ('JSONIFY_MIMETYPE', 'application/json'),
        ('EXPLAIN_TEMPLATE_RELOADING', False), ('TEMPLATES_AUTO_RELOAD', True),
        ('MAX_COOKIE_SIZE', 4093),
        #custom vairables
        ('SQLALCHEMY_DATABASE_URL', ''), ('SQLITE_DATABASE_URL', 'sqlite:///test.db'),
        ('POSTGRES_DATABASE_URL', "postgresql://localhost:5432/testdb")
    ]

class TestingConfig(DefaultConfig):
    def __init__(self):
        "noop"
    ENV = ConfigItem('development')
    TESTING = ConfigItem(True)
    DEBUG = ConfigItem(True)
    SQLALCHEMY_DATABASE_URI = ConfigItem('sqlite://test-' + __class__.APP_NAME + '.db')

class DevelopmentConfig(DefaultConfig):
    pass

class ProductionConfig(DefaultConfig):
    pass