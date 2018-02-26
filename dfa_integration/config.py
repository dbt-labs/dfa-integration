import json

from dfa_integration.logger import GLOBAL_LOGGER as logger


def validate_config(config):
    required_keys = ['refresh_token', 'client_id', 'client_secret',
                     'user_agent', 'reports']
    missing_keys = []
    null_keys = []
    has_errors = False

    for required_key in required_keys:
        if required_key not in config:
            missing_keys.append(required_key)

        elif config.get(required_key) is None:
            null_keys.append(required_key)

    if len(missing_keys) > 0:
        logger.fatal("Config is missing keys: {}"
                     .format(", ".join(missing_keys)))
        has_errors = True

    if len(null_keys) > 0:
        logger.fatal("Config has null keys: {}"
                     .format(", ".join(null_keys)))
        has_errors = True

    if has_errors:
        raise RuntimeError


def load_config(filename):
    config = {}

    try:
        with open(filename) as f:
            config = json.load(f)
    except:
        logger.fatal("Failed to decode config file. Is it valid json?")
        raise RuntimeError

    validate_config(config)

    return config
