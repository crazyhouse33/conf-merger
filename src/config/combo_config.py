from config.base_config import Config

class Combo_Config(Config):
    def __init__(self, path):
        super().__init__(path)
        self.configs =  self.name.split('-')
        assert len(self.configs) >= 2, "Combo config file {} should have at least two base configs".format(path)

    def satisfied_by(self, config_list):
        return all( config in map(str,config_list) for config in self.configs )
        
