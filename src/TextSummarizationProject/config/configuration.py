from TextSummarizationProject.constants import *
from TextSummarizationProject.utils.common import read_yaml, create_directories
from TextSummarizationProject.entity import (DataIngestionConfig,DataValidationConfig)

class ConfigurationManager:
    def __init__(self, 
                 config_filepath: Path = CONFIG_FILE_PATH, 
                 params_filepath: Path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artefacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )

            return data_ingestion_config
        
        except Exception as e:
            raise e
    
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            config = self.config.data_validation

            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                status_file=config.status_file,
                all_required_files=config.all_required_files
            )

            return data_validation_config
        
        except Exception as e:
            raise e