from src.AIDRP.config.configuration import ConfigurationManager
from src.AIDRP.components.data_validation import DataValidation
from src.AIDRP.logging import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        # Initialize the DataValidationTrainingPipeline
        pass

    def main(self):
        # Main function to execute data validation pipeline
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        
        # Perform data validation on all columns
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log and raise exceptions
        logger.exception(e)
        raise e
