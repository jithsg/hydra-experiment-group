import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="./configs/", config_name="config", version_base='1.2')
def main(config: DictConfig)-> None:
    print(OmegaConf.to_yaml(config))
    
    
    
if __name__ == "__main__":
    main()
    
