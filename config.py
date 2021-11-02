import os 

class Config(object):
   API_ID = int(os.env_sample.get("API_ID", 6)) 
   API_HASH = os.env_sample.get("API_HASH", "") 
   TOKEN = os.env_sample.get("TOKEN" "")
