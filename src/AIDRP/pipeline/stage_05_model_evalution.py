from AIDRP.logging import logger
from AIDRP.config.configuration import ConfigurationManager
from AIDRP.components.model_evalution import ModelEvalution


STAGE_NAME = "Model Evalution Stage"

class ModelEvalutionTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        model_evalution_config = config.get_model_evalution_config()
        model_evalution_config = ModelEvalution(model_evalution_config)
        model_evalution_config.save_result()



if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvalutionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
