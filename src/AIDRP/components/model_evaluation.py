from sklearn.metrics import f1_score
import pandas as pd  
import joblib
from src.AIDRP.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from src.AIDRP.utils.common import save_json


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        """Evaluate F1 score"""
        f1 = f1_score(actual, pred, average='micro')
        return f1

    def save_results(self):
        """Evaluate model on test data and save metrics"""
        
        # Load test data
        test_data = pd.read_csv(self.config.test_data_path)
        
        # Load trained model
        model = joblib.load(self.config.model_path)  

        # Extract X, y test data
        X_test = test_data.drop([self.config.target_column], axis=1)  
        y_test = test_data[[self.config.target_column]]

        # Make predictions
        predicted = model.predict(X_test)
        
        # Evaluate F1 score
        f1 = self.eval_metrics(y_test, predicted)

        # Save metrics
        metrics = {"F1 Score": f1}
        save_json(path=Path(self.config.metric_file_name), data=metrics)