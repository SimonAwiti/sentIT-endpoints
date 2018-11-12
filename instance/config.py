import os


"""Application configuration"""

class Config(object):
    """Base config class"""
    DEBUG = True
    SECRET = os.getenv("SECRET_KEY")

class DevelopmentConfig(Config):
    """Development configurations"""
    DEBUG = True

class TestingConfig(Config):
    """Testing configurations"""
    DEBUG = True
    TESTING = True
    SECRET_KEY = "SECRET"

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


