from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    # Configuration for data ingestion
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    # Configuration for data validation
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    # Configuration for data transformation
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    # Configuration for model training
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    iterations: int
    learning_rate: float
    depth: int
    l2_leaf_reg: float
    bootstrap_type: str
    random_strength: float
    bagging_temperature: float
    od_type: str
    od_wait: int
    target_column: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    # Configuration for model evaluation
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
