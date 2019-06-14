import pandas as pd
import time
from concurrent import futures
import os

INPUT_PATH = 'data/input/'
OUTPUT_PATH = 'data/output/'

def to_txt(row):
    file_content = '\n'.join([str(row.ID), str(row.Question), str(row.Answer)])
    try:
        with open(os.path.join(OUTPUT_PATH, str(row.ID) + '.txt'), 'w+') as file:
            file.writelines(file_content)
    except Exception as e:
        print(f'Could not process question {row.Question}')
        pass

def convert(path, file_list):

    try:
        for file in file_list:
            content = pd.read_csv(os.path.join(path, file), encoding='ISO-8859-1')

            with futures.ThreadPoolExecutor() as executor:
                executor.map(to_txt, content.itertuples())

    except Exception as e:
        print(f'Error occurred while processing {file}')
        pass

if __name__ == '__main__':

    start = time.time()

    input_files = os.listdir(INPUT_PATH)
    convert(INPUT_PATH, input_files)

    end = time.time()

    print(f'Total time taken in seconds : {end - start}')