from functools import wraps
import logging

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"---- Function {func.__name__} Enter ----")
        result = func(*args, **kwargs)
        logger.info(f"---- Function {func.__name__} Exit ----")
        return result

    return wrapper
