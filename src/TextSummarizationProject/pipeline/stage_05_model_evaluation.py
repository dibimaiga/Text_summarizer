from TextSummarizationProject.config.configuration import ConfigurationManager
from TextSummarizationProject.components.model_evaluation import ModelEvaluation

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        model_evaluation_config = config_manager.get_model_evaluation_config()

        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
