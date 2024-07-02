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
    Reads YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.

    Returns:
        ConfigBox: ConfigBox object containing the YAML content.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML file: {path_to_yaml}")
        raise e


def create_directories(path_to_directories: list[Path]) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list[Path]): List of directory paths to create.

    Returns:
        None
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created: {path}")
    except Exception as e:
        raise e


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of the file.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
