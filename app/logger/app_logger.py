import os
import sys
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

LOG_FILE = os.getenv("LOG_FILE", "app.log")

logger.remove()

logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

if LOG_FILE:
    logger.add(
        LOG_FILE,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        level="INFO",
        rotation="20 MB",
        retention=10,
        compression="zip",
        encoding="utf-8"
    )
