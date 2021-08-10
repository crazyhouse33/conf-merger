from abc import ABC, abstractstaticmethod
from config.virtual_config import Virtual_config
import sys

class Config(ABC,Virtual_config):

    @classmethod
    def merge(cls,configs, dest):
       if not configs:
           print( "No config to merge", file=sys.stderr) 
           sys.exit(0) 
       else:
           return cls._merge(configs, dest)

    @abstractstaticmethod
    def _merge(configs, dest):
        pass


