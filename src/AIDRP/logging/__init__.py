from pathlib import Path
import sys
import logging

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "logs"

log_filepath = Path(Path(log_dir)/"running_log.log")
log_filepath.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("AIDRP_logger")