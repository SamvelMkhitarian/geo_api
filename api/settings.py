from dotenv import load_dotenv
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
env_file_path = os.path.join(BASE_DIR, '.env')
load_dotenv(env_file_path)


DATABASE = os.getenv('DATABASE')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
API_KEY = os.getenv('API_KEY')
FORMAT = os.getenv('FORMAT')
GEO_URL = os.getenv('GEO_URL')
