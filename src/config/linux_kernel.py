from pathlib import Path
import os 
import sys
from config.base_config import Config

class Linux_kernel_conf(Config):
    merge_script=None

    @staticmethod
    def set_merger_path(path):
        Linux_kernel_conf.merge_script=path

    @staticmethod
    def _merge(configs, dest):
        configs_str = ' '.join([config.path for config in configs])
        parent_dir = Path(dest).parent
        parent_dir.mkdir(parents=True, exist_ok=True)
        merging_command = ' '.join([Linux_kernel_conf.merge_script, '-m -r -y -O', str(parent_dir), configs_str] )
        ret = os.WEXITSTATUS(os.system(merging_command))
        if ret:
            sys.exit(f"{merging_command} failed with status {ret}", file=sys.stderr)
        os.rename(parent_dir / '.config', dest)
        return ret

