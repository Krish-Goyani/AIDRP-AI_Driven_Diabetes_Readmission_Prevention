import pandas as pd
from src.AIDRP.entity.config_entity import DataValidationConfig 

class DataValidation:

    def __init__(self, config: DataValidationConfig):
        # Store configuration
        self.config = config  

    def validate_all_columns(self) -> bool:
        
        # Validation status variable
        validation_status = None  
        
        try:
            # Read data
            data = pd.read_csv(self.config.unzip_data_dir)
            
            # Get all column names
            all_cols = list(data.columns)

            # Get expected column names from config 
            all_schema = self.config.all_schema.keys()

            # Validate each column
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
            
        except Exception as e:
            raise e