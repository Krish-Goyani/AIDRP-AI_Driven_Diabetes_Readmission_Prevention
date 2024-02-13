# Imports
import urllib.request as request
import zipfile
from src.AIDRP.logging import logger  
from src.AIDRP.utils.common import get_size
from src.AIDRP.entity.config_entity import DataIngestionConfig
from pathlib import Path

# Data ingestion class 
class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        """
        Constructor to initialize class with config
        """
        self.config = config

    def download_file(self):
        """
        Download raw data file from source url if not already present
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, 
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with headers: {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts downloaded zip file into unzip directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)