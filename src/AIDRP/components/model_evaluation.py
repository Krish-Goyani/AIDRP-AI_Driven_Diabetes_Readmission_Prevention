from sklearn.metrics import f1_score
import pandas as pd
import joblib
from src.AIDRP.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from src.AIDRP.utils.common import save_json


class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig) :
        self.config = config

    def eval_metrics(self,actual,pred):
        f1 = f1_score(actual,pred,average='micro')
        return f1
    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        predicted_values = model.predict(X_test)

        f1 = self.eval_metrics(y_test,predicted_values)

        # Saving metrics as local
        score = {"F1 Score" : f1}
        save_json(path=Path(self.config.metric_file_name), data=score)