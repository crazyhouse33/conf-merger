import glob
from config.base_config import Config
from config.combo_config import Combo_Config
import sys

#Retrieve configs from a fs

def get_config(path):
    return Config(path)

def extract_configs_from_fs(conf_dir, selection):
    configs=glob.glob(f"{conf_dir}/**/*.conf", recursive=True)

    combos = []
    regulars= [] 
    
    # Filtering out combos. List allow on fly deletion
    for  i, conf in list(enumerate(configs)):
        if '/combo/' in conf:
            del(configs[i-len(combos)])
            combos.append(Combo_Config(conf))


    for selected in selection:
        matching = [ config for config in configs if config.endswith(f"/{selected}.conf") ]
        if not matching:
            sys.exit(f"Config {selected} not found in {conf_dir}")

        # TODO make this check for the whole config folder beforehand instead (more convenient to early detect bugs)
        elif len(matching) > 1: 
            sys.exit("Ambigious config name:\n\t{}".format('\n\t'.join(matching)))

        regulars.append(get_config(matching[0]))
        
    return regulars, combos

