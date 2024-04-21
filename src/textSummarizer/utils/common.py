import os
from tabnanny import verbose
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args: path_to_yaml: Path like input

    Raises: ValueError: if yaml file is empty

    Returns: ConfigBox: ConfigBox object

    """

    try:
        with open('path_to_yaml') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("ya,l file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML file: {path_to_yaml}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """
    creates directories if they do not exist

    Args: path_to_directories: list of paths

    Returns: None

    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    returns size of file

    Args: path: Path like input

    Returns: str: size of file

    """

    size_in_kb = round(os.pth.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
