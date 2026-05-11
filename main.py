from TextSummarizationProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from TextSummarizationProject.pipeline.stage_02_data_validation import DataValidationPipeline
from TextSummarizationProject.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x") 
except Exception as e:
    logger.exception(e)
    raise e