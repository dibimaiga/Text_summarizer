import os
from box.exceptions import BoxValueError
import yaml
from box import ConfigBox
from pathlib import Path
from TextSummarizationProject.logging import logger

def read_yaml(path_to_yaml: Path) -> ConfigBox: #configbox for easily accessing the content of my yml(in a form of dict) file
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

def create_directories(path_to_directories: list):
    """
    Creates a list of directories if they don't exist.

    Args:
        path_to_directories (list): A list of paths to directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory: {path} created successfully")


def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"