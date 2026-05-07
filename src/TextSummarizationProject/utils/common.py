import os
from box.exceptions import BoxValueError
import yaml
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from TextSummarizationProject import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Returns:
        ConfigBox: A ConfigBox object containing the yaml data.
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
    return ConfigBox(content)