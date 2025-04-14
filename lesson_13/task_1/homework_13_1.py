from pathlib import Path
import csv

path_result_shershen = Path('result_shershen.csv')
path_first_file = Path('work_with_csv/random-michaels.csv')
path_second_file = Path('work_with_csv/random.csv')

with open(path_result_shershen, 'w', newline='') as new_file:
    writer = csv.writer(new_file)


def compare_for_duplicates_csv(path_file):
    """Appends unique data from given csv-file to file 'result_shershen.csv'
    :param path_file: path for a given file
    """
    result_id_list = []
    with open(path_result_shershen, newline='') as result_file:
        reader_result_file = csv.reader(result_file)
        for row in reader_result_file:
            result_id_list.append(row[0])

    with open(path_file, newline='') as input_file:
        reader_input_file = csv.reader(input_file)
        for row in reader_input_file:
            if row[0] not in result_id_list:
                with open(path_result_shershen, 'a', newline='') as result_file:
                    writer_result_file = csv.writer(result_file)
                    writer_result_file.writerow(row)
                    result_id_list.append(row[0])


compare_for_duplicates_csv(path_first_file)
compare_for_duplicates_csv(path_second_file)
