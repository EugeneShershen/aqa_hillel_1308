from datetime import datetime, timedelta
from pathlib import Path
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.FileHandler("hb_test.log")
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def count_lines(path_to_file):
    with open(path_to_file, 'r') as file:
        for count, line in enumerate(file):
            pass

        return count


def read_each_row(path_to_file):
    with open(path_to_file, 'r') as file:
        for row in file:
            yield row.strip()


def logs_for_work(path_to_file):
    logs_list = []
    gen = read_each_row(path_to_file)

    for _ in range(count_lines(path)):
        row = next(gen)
        if 'Key TSTFEED0300|7E3E|0400' in row:
            logs_list.append(row)

    return logs_list


def analyze_log_file(path_to_file):
    work_list = logs_for_work(path_to_file)

    for i, row in enumerate(work_list):
        if i == 0:
            continue

        prev_row = work_list[i - 1]

        start_index = row.find("Timestamp ") + 10
        end_index = row.find("Timestamp ") + 18

        prev_row_time = prev_row[start_index:end_index]
        current_row_time = row[start_index:end_index]

        prev_time = datetime.strptime(prev_row_time, "%H:%M:%S")
        cur_time = datetime.strptime(current_row_time, "%H:%M:%S")

        difference_time = prev_time - cur_time

        if timedelta(seconds=31) < difference_time < timedelta(seconds=33):
            logger.warning(f"Heartbeat is between 31 and 33 seconds!\n"
                           f"Previous Timestamp: {prev_time.time()}\n"
                           f"Next Timestamp: {cur_time.time()}\n")

        elif difference_time >= timedelta(seconds=33):
            logger.error(f"Heartbeat is equal or greater than 33 seconds!\n"
                         f"Previous Timestamp: {prev_time.time()}\n"
                         f"Next Timestamp: {cur_time.time()}\n")


if __name__ == "__main__":
    path = Path('hblog.txt')
    analyze_log_file(path)
