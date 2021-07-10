from pathlib import Path
import os 
import sys

class Virtual_config():

    def __init__(self, path):
        name = os.path.basename(path)
        self.name = name[:name.rindex(".conf")]
        self.path=path

    def __str__(self):
        return self.path

    def __repr__(self):
        return f"<{type(self).__qualname__}> {self.name}" 
