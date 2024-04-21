import os
import sys
import logging

logging_str = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "text_summarizer.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("text_summarizer_logger")
