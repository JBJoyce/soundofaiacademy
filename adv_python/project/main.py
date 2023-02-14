import math
import sqlite3
import os
from pathlib import Path

from storing.createdb import create_db
from threadeddatapipeline import ThreadedDataPipeline
from utils import create_file_paths_from_dir, nest_list
from datapipeline import create_hardcoded_data_pipeline



NUM_THREADS = 10

def main():
    create_db("/home/jbjoyce/soundofaiacademy/adv_python/project/test.db")

    # create necessary resources
    paths = create_file_paths_from_dir(Path("/home/jbjoyce/soundofaiacademy/adv_python/project/samplefiles"))
    nested_list_length = math.ceil(len(paths) / NUM_THREADS)
    nested_paths = nest_list(paths, nested_list_length)
    data_pipelines = [create_hardcoded_data_pipeline() for i in range(NUM_THREADS)]

    # run pipelines in multiple threads
    threads = []
    for data_pipeline, paths in zip(data_pipelines, nested_paths):
        threads.append(ThreadedDataPipeline(data_pipeline, paths))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # fetch db entries and print them
    connection = sqlite3.connect("/home/jbjoyce/soundofaiacademy/adv_python/project/test.db")
    cursor = connection.cursor()
    cursor.execute("SELECT NAME, CURRENCY, PRICE FROM PRODUCT")
    products = cursor.fetchall()
    print(products)
    print(len(products))

    # remove db
    os.remove("/home/jbjoyce/soundofaiacademy/adv_python/project/test.db")


if __name__ == "__main__":
    main()
