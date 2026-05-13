from TextSummarizationProject.config.configuration import ConfigurationManager
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config() # so that i've access to my model and tokenizer path

    def predict(self, text: str) -> str:
        # Load the model and tokenizer
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        # Tokenize the input text
        inputs = tokenizer(text, max_length=128, truncation=True, padding="max_length", return_tensors="pt")

        print("\nInput Text:\n", text)
        
        # Generate the summary
        summary_ids = model.generate(input_ids=inputs["input_ids"], attention_mask=inputs["attention_mask"],
                                     length_penalty=0.8, num_beams=8, max_length=128)

        # Decode the generated summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        summary = summary.replace("", " ")

        print("\nGenerated Summary:\n", summary)

        return summary