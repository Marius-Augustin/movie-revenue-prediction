import os
from dotenv import load_dotenv

class Config:
  def __init__(self):
    load_dotenv()
    env_vars = {
      'DB_HOST':       os.getenv('DB_HOST'),
      'DB_DATABASE':   os.getenv('DB_DATABASE'),
      'DB_USER':       os.getenv('DB_USER'),
      'DB_PASS':       os.getenv('DB_PASS'),
      'TMDB_BASE_URL': os.getenv('TMDB_BASE_URL'),
      'TMDB_API_KEY':  os.getenv('TMDB_API_KEY'),
    }

    for name, value in env_vars.items(): 
      if value is None:
        raise Exception(f'Environment value {name} not loaded.')
      setattr(self, name, value)