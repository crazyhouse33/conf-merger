from pathlib import Path
import os 
import sys

class Config():
    merge_script=None

    @staticmethod
    def set_merger_path(path):
        Config.merge_script=path

    @staticmethod
    def merge_configs(configs, dest):
        configs_str = ' '.join([config.path for config in configs])
        parent_dir = Path(dest).parent
        parent_dir.mkdir(parents=True, exist_ok=True)
        merging_command = ' '.join([Config.merge_script, '-m -r -y -O', str(parent_dir), configs_str] )
        ret = os.WEXITSTATUS(os.system(merging_command))
        if ret:
            print (f"{merging_command} failed with status {ret}", file=sys.stderr)
            sys.exit(ret)
        os.rename(parent_dir / '.config', dest)
        return ret

    def __init__(self, path):
        name = os.path.basename(path)
        self.name = name[:name.rindex(".conf")]
        self.path=path

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{type(self).__qualname__}> {self.name}" 
