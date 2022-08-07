import yaml
from housing.exception import HousingException
import os , sys

####util is a script containing all helper functions not used in pipeline

def read_yaml_file(file_path:str) -> dict:
    
    try:
        
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise HousingException(e,sys) from e
    
    
    
