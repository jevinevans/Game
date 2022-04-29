from loguru import logger

logger.add("./logs/character.log", rotation="10 MB", retention=5)
