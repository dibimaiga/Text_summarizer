from TextSummarizationProject.config.configuration import ConfigurationManager
from TextSummarizationProject.components.data_validation import DataValidation
from TextSummarizationProject.logging import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files()
