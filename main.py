from kidneyClassifier import logger
from kidneyClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidneyClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from kidneyClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "Preparing Base Model Stage"

# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     obj = PrepareBaseModelPipeline()
#     obj.main()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e