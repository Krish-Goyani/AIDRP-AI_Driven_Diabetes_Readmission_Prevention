import joblib
from pathlib import Path


class PredictionPipeline:
    def __init__(self) -> None:
        # Initialize PredictionPipeline with a pre-trained model
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        # Make predictions using the pre-trained model
        prediction = self.model.predict(data)

        return prediction
