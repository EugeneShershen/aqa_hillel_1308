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
    with open(path_file, newline='') as output_file:
        reader_output_file = csv.reader(output_file)

        for row in reader_output_file:

            with open(path_result_shershen, newline='') as input_file:
                reader_input_file = csv.reader(input_file)
                temp_list_id = []

                for element in reader_input_file:
                    list_el = list(element)
                    temp_list_id.append(list_el[0])

            if row[0] in temp_list_id:
                pass
            else:
                with open(path_result_shershen, 'a', newline='') as input_file:
                    writer_input_file = csv.writer(input_file)
                    writer_input_file.writerow(row)


compare_for_duplicates_csv(path_first_file)
compare_for_duplicates_csv(path_second_file)
