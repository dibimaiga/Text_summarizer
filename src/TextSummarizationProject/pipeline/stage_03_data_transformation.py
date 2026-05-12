from TextSummarizationProject.logging import logger
from TextSummarizationProject.config.configuration import ConfigurationManager
from TextSummarizationProject.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()    
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
