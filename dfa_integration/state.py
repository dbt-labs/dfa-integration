import json
import os.path

from dateutil.parser import parse

from dfa_integration.logger import GLOBAL_LOGGER as logger


def get_last_record_value_for_report(state, profile_id, report_id):
    last_value = state.get('bookmarks', {}) \
                      .get(str(profile_id), {}) \
                      .get(str(report_id))

    if last_value is None:
        return None

    return parse(last_value)


def incorporate(state, profile_id, report_id, value):
    if value is None:
        return state

    new_state = state.copy()

    parsed = value.strftime("%Y-%m-%d %H:%M:%S")

    if 'bookmarks' not in new_state:
        new_state['bookmarks'] = {}

    if str(profile_id) not in new_state['bookmarks']:
        new_state['bookmarks'][str(profile_id)] = {}

    last_record = get_last_record_value_for_report(
        state, profile_id, report_id)

    if(last_record is None or last_record < value):
        new_state['bookmarks'][str(profile_id)][str(report_id)] = parsed

    return new_state


def save_state(state, filename):
    if not state:
        return

    if filename is None:
        logger.warn('No state file specified, not writing state!')

    logger.info('Updating state.')

    with open(filename, 'w') as handle:
        return json.dump(state, handle)

    return state


def load_state(filename):
    if filename is None or not os.path.isfile(filename):
        return {}

    try:
        with open(filename) as handle:
            return json.load(handle)
    except:
        logger.fatal("Failed to decode state file. Is it valid json?")
        raise RuntimeError
