import pandas as pd
import os
from src.AIDRP.logging import logger
from sklearn.linear_model import ElasticNet
import joblib
import catboost
from src.AIDRP.config.configuration import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        params={'iterations': self.config.iterations, 'learning_rate': self.config.learning_rate,
                 'depth': self.config.depth, 'l2_leaf_reg': self.config.l2_leaf_reg, 
                 'bootstrap_type': self.config.bootstrap_type, 'random_strength': self.config.random_strength,
                   'bagging_temperature': self.config.bagging_temperature, 'od_type': self.config.od_type, 'od_wait': self.config.od_wait}

        cb = catboost.CatBoostClassifier(**params,random_state=42,verbose=False)
        cb.fit(train_x, train_y)

        joblib.dump(cb, os.path.join(self.config.root_dir, self.config.model_name))

        