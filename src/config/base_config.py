from abc import ABC, abstractstaticmethod
from config.virtual_config import Virtual_config

class Config(ABC,Virtual_config):

    @abstractstaticmethod
    def merge(configs, dest):
        pass

    
