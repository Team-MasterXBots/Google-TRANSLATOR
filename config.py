import os 

class Config(object):
   API_ID = int(os.environ.get("API_ID", 6)) 
   API_HASH = os.environ.get("API_HASH", "") 
   TOKEN = os.environ.get("TOKEN" "")
