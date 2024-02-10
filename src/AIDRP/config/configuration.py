from src.AIDRP.constants import *
from src.AIDRP.utils.common import read_yaml,create_directories

from src.AIDRP.entity.config_entity import DataIngestionConfig,DataValidationConfig,ModelEvalutionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion 
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation 
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE= config.STATUS_FILE,
            all_schema= schema
        )


        return data_validation_config
    




    def get_model_evalution_config(self)->ModelEvalutionConfig:
        config = self.config.model_evalution
        params = self.params.CatBoostClassifier
        schema = self.schema.TARGET_COLUMN

        model_evalution_config = ModelEvalutionConfig(
            root_dir= config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name,
            all_params=params,
            schema = schema.readmitted
        )

        return model_evalution_config
        