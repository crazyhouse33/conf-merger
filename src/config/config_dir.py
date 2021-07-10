import glob
from config.linux_kernel import Linux_kernel_conf
from config.combo_config import Combo_config
import sys
import os.path
from pathlib import Path

default_dir = Path(__file__).parent.parent / 'default-confs'

class_matcher = {"linux-kernel" : Linux_kernel_conf}
 
# Represent a configuration folder, from wich you retrieves all kinds of conf files

class Config_dir:
    
    def __init__(self, path, config_class=None):

        if not os.path.isdir(path):
            default = default_dir / path
            if os.path.isdir(default):
                path = default
            else:
                sys.exit("Cant find specified configuration folder: {path}")
        self.path=path
        if config_class:
            self.config_class = class_matcher[config_class]
        else:
            self.config_class = class_matcher[os.path.basename(path)]
        self.combos, self.others = self.__extract_confs_from_fs()

    def __extract_confs_from_fs(self):
        config_files=glob.glob(f"{self.path}/**/*.conf", recursive=True)
        combos=[]
        regulars=[]

        while config_files:
            path = config_files.pop()
            relative= './' + os.path.relpath(path, self.path)
            if '/combo/' in relative:
                combos.append(Combo_config(path))
            else:
                regulars.append( path )
        return combos, regulars

    def __matching_configs(self, name): 
        return [ config for config in self.others if config.endswith(f"/{name}.conf") ]

    def get_configs(self, selection):
        ret=[]

        for selected in selection:
            matching = self.__matching_configs(selected)
            if not matching:
                sys.exit(f"Config {selected} not found in {self.path}")
            elif len(matching) > 1: 
                sys.exit("Ambigious config name:\n\t{}".format('\n\t'.join(matching)))
            ret.append(self.config_class(matching[0]))
        return ret

    def get_triggered_combos(self, selection):
        triggered_combos=[]
        for combo in self.combos:
            if combo.satisfied_by(selection):
                    triggered_combos.append(combo)
        return triggered_combos

    def merge(self, other):
        if self.config_class != other.config_class:
            sys.exit(f"Type error: cant mix {self.path} of type {self.config_class} with {other.path} of type {other.config_class}")
        self.combos.extend(other.combos)
        self.others.extend(other.others)

    def check(self):
        for i in range(len(self.other)):
            for j in range(i-1):
                if pathlib.part( self.other[i])[-1] == pathlib.part( self.other[j])[-1]:
                    sys.exit( f"Name colision: {self.other[i]} and {self.other[j]}" )





