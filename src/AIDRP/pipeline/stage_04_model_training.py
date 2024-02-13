from src.AIDRP.config.configuration import ConfigurationManager
from src.AIDRP.components.model_trainer import ModelTrainer
from src.AIDRP.logging import logger

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        # Initialize the ModelTrainerTrainingPipeline
        pass

    def main(self):
        # Main function to execute model training pipeline
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        
        # Train the model
        model_trainer.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log and raise exceptions
        logger.exception(e)
        raise e
