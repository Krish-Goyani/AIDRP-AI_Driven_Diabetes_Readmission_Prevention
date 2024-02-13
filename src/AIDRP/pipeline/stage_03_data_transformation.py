from src.AIDRP.logging import logger
from src.AIDRP.config.configuration import ConfigurationManager
from pathlib import Path
from src.AIDRP.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        # Initialize the DataTransformationTrainingPipeline
        pass

    def main(self):
        try:
            # Read status from the validation process
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                # Execute data transformation if validation is successful
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.data_transformation()

            else:
                raise Exception("Your data schema is not valid")

        except Exception as e:
            # Log and print exceptions
            logger.exception(e)
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e