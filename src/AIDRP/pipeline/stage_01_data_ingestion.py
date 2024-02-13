from src.AIDRP.config.configuration import ConfigurationManager
from src.AIDRP.components.data_ingestion import DataIngestion
from src.AIDRP.logging import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        # Initialize the DataIngestionTrainingPipeline
        pass

    def main(self):
        # Main function to execute data ingestion pipeline
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        
        # Perform data download and extraction
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log and raise exceptions
        logger.exception(e)
        raise e
