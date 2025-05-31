from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

# logger.info("This test log message")

def divide_no(a,b):
    try:
        logger.info("Dividing a by b")
        return a/b
    except Exception as e:
        logger.error("Error occured")
        raise CustomException(e, sys)


if __name__ == "__main__":
    try: 
        logger.info("Starting main program")
        divide_no(10,2)
    except CustomException as ce:
        logger.error(str(ce))
        # raise CustomException(e, sys)
    
    logger.info("Ending main program")

 