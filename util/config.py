import openai
from jproperties import Properties

configs = Properties()

def get_configuration():    
    return configs

def load_configuration(filename: str):    
    with open(filename, 'rb') as config_file:
        configs.load(config_file)

    openai.api_type = configs.get("API_TYPE").data
    openai.api_base = configs.get("API_BASE").data 
    openai.api_version = configs.get("API_VERSION").data
    openai.api_key = configs.get("API_KEY").data 

    return configs
