from src.AIDRP.logging import logger
from src.AIDRP.config.configuration import ConfigurationManager
from src.AIDRP.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        # Initialize the ModelEvaluationTrainingPipeline
        pass

    def main(self):
        # Main function to execute model evaluation pipeline
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        
        # Save evaluation results
        model_evaluation.save_results()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log and raise exceptions
        logger.exception(e)
        raise e
