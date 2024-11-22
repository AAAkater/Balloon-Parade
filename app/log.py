import logging
import sys
from logging import Logger

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - \033[32m%(levelname)s\033[0m - %(message)s",
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
        # logging.FileHandler("app.log", mode="a"),
    ],
)

logger: Logger = logging.getLogger("fastapi")
