from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('json_shershen.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


dir_json_path = Path('work_with_json/')


def is_all_files_json(dir_path):
    """Checks files the in given directory for '.json'-extension
    :param dir_path: path for a given directory
    """

    all_files = [file for file in dir_path.iterdir() if file.is_file()]

    for file in all_files:
        log_message_info = f'{file.name} is valid'
        log_message_error = f'{file.name} is invalid'

        try:
            with open(file, 'r', encoding='utf-8') as cur_file:
                data = json.load(cur_file)
            logger.info(log_message_info)
        except json.JSONDecodeError:
            logger.error(log_message_error)


is_all_files_json(dir_json_path)
