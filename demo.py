from src.logger import logging
import sys
from src.exception import MyException

try:
    s=10/0
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e