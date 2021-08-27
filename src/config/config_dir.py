import glob
from config.linux_kernel import Linux_kernel_conf
from config.combo_config import Combo_config
from config.group_config import Group_config
import sys
import os.path
from pathlib import Path
from collections import OrderedDict
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
                sys.exit(f"Cant find specified configuration folder: {path}")
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
                combos.append( Combo_config(path))
            elif '/alias/' in relative:
                regulars.append(Group_config(path))
            else:
                regulars.append( self.config_class(path) )
        return combos, regulars

    def __get_first_matching(self, name): 
        for config in self.others:
            if config.name == name:
                return config
        sys.exit(f"Config {name} not found in {self.path}")

    def get_configs(self, selection):
        ret=[]
        for selected in selection:
            matching = self.__get_first_matching(selected)
            if isinstance(matching, Group_config):
                ret.extend(self.get_configs(matching.get_members()))
            else:
                ret.append(matching)
        return ret

    def get_triggered_combos(self, selection):
        triggered_combos=[]
        for combo in self.combos:
            if combo.satisfied_by(selection):
                    triggered_combos.append(combo)
        return triggered_combos 

    def check(self):
        for i in range(len(self.other)):
            for j in range(i-1):
                if pathlib.part( self.other[i])[-1] == pathlib.part( self.other[j])[-1]:
                    sys.exit( f"Name colision: {self.other[i]} and {self.other[j]}" )

    def merge(self, other):
           if self.config_class != other.config_class:
               sys.exit(f"Type error: cant mix {self.path} of type {self.config_class} with {other.path} of type {other.config_class}")
           self.combos.extend(other.combos)
           self.others.extend(other.others)

    def remove_combos_doublons(self):
        seen = {}
        new = []
        for combo in self.combos:
            if not combo.name in seen:
                new.append(combo)
            seen[combo.name] = True
        self.combos = new





