from config.virtual_config import Virtual_config

class Group_config(Virtual_config):

    def get_members(self):
        with open(self.path) as f:
            return filter(None,f.read().splitlines())
        
