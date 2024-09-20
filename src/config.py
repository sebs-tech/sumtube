
class SumTubeConfig:
    def __init__(self, config):
        self.config_file_path = config
        self.config_file = []
       
    def load_config_file(self):
        print(self.config_file_path)
        
        
        
        

if __name__ == "__main__":
    
    cfg = SumTubeConfig('config.txt')
    cfg.load_config_file()