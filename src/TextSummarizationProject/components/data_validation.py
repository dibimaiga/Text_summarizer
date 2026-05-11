import os
from TextSummarizationProject.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files(self) -> bool:
        try:
            status = None

            all_files = os.listdir(os.path.join("artefacts", "data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.all_required_files:
                    status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {status}")

                else:
                    status = True
                    
                    with open(self.config.status_file, "w") as f:     
                        f.write(f"Validation status: {status}")
                        
            return status
        
        except Exception as e:
            raise e