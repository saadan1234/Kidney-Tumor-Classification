from kidneyClassifier.components.model_evaluation import Evaluation
from kidneyClassifier.config.configuration import ConfigurationManager
from kidneyClassifier import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try: 
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=============x")
    except Exception as e:
        logger.exception(e)
        raise e






