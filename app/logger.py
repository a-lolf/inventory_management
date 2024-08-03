from loguru import logger

logger.add("logs/api.log", rotation="500 MB")
