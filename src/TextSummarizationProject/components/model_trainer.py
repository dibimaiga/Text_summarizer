from transformers import Trainer, TrainingArguments
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_dataset, load_from_disk
from transformers import DataCollatorForSeq2Seq
import torch
import os
from TextSummarizationProject.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_checkpoint)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_checkpoint).to(device)
        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        dataset = load_from_disk(self.config.data_path)


        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.eval_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            processing_class=tokenizer,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"],
            data_collator=data_collator
        )
        trainer.train()

        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))

        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))