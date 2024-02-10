from src.AIDRP.logging import logger
from src.AIDRP.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.AIDRP.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


from src.AIDRP.pipeline.stage_05_model_evalution import ModelEvalutionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Model evalution Stage"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      model_evalution = ModelEvalutionTrainingPipeline()
      model_evalution.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
      