import pandas as pd
import joblib
import catboost

from src.AIDRP.logging import logger  
from src.AIDRP.entity.config_entity import ModelTrainerConfig


class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        """Train CatBoost model on training data"""
        
        # Load training data
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        # Extract X, y from dataframes
        X_train = train_df.drop([self.config.target_column], axis=1)
        y_train = train_df[[self.config.target_column]]

        X_test = test_df.drop([self.config.target_column], axis=1)
        y_test = test_df[[self.config.target_column]]

        # CatBoost parameters
        params = {'iterations': self.config.iterations, 
                  'learning_rate': self.config.learning_rate,
                  'depth': self.config.depth, 
                  'l2_leaf_reg': self.config.l2_leaf_reg,
                  'bootstrap_type': self.config.bootstrap_type,
                  'random_strength': self.config.random_strength,
                  'bagging_temperature': self.config.bagging_temperature,
                  'od_type': self.config.od_type,
                  'od_wait': self.config.od_wait}

        # Train model
        model = catboost.CatBoostClassifier(**params, 
                           random_state=42, verbose=False)
        model.fit(X_train, y_train)

        # Save trained model
        joblib.dump(model, os.path.join(self.config.root_dir, 
                                       self.config.model_name))