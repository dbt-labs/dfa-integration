import logging
import sys
import warnings

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(logging.Formatter('%(message)s'))
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(
    logging.Formatter('%(asctime)-15s %(message)s'))

logger = logging.getLogger('dfa_integration')
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)

logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger('httplib2').setLevel(logging.CRITICAL)

GLOBAL_LOGGER = logger

warnings.filterwarnings("ignore")
