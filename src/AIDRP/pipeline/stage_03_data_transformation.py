import os 
import pandas as pd

from src.AIDRP.logging import logger
from src.AIDRP.config.configuration import ConfigurationManager
from pathlib import Path
from src.AIDRP.components.data_transformation import DataTransformation
STAGE_NAME = 'data transformation stage'

class DataTransformationTrainingPipeline:
    def _init_(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.preprocessing()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)

if __name__ == '_main_':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e