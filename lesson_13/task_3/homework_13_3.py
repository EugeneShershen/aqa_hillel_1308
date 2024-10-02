from pathlib import Path
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


file_path = Path('work_with_xml/groups.xml')


def get_incoming_value(path, num):
    root = ET.parse(path).getroot()

    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == num:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    log_message_info = f'Number: {number.text}; Incoming: {incoming.text}'
                    logger.info(log_message_info)
                else:
                    logger.error('Parameter "incoming" doesn\'t exist!!!')
            else:
                logger.error('Parameter "timingExbytes" doesn\'t exist!!!')
        elif number is None:
            logger.error('Parameter "number" doesn\'t exist!!!')


get_incoming_value(file_path, '0')
