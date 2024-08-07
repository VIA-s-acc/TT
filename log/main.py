"""
LEVEL NAME | SEVERITY VALUE | METHOD    
TRACE           5              .trace
DEBUG           10             .debug
INFO            20             .info
SUCCESS         25             .success
WARNING         30             .warning
ERROR           40             .error
CRITICAL        50             .critical
"""
import sys
from loguru import logger

logger.remove(0)
logger.add('logs.log', level="DEBUG", rotation='1 MB', retention='1 week')
logger.add(sys.stderr, level = "DEBUG")


@logger.catch
def div(num: int = 0):
    return 1/num

def main():
    logger.trace("Trace MSG")
    logger.debug("Debug MSG")
    logger.info('Info msg')
    logger.success("Success msg")
    logger.warning("Warning MSG")
    logger.error("Error MSG")
    logger.critical("Critical MSG")
    
    div(num = 0)
    
if __name__ == "__main__":
    main()
    
    