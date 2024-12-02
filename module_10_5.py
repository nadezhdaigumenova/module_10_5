from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        file = file.readline()
        for line in file:
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f'{end_time - start_time} (линейный)')


    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'{end_time - start_time} (многопроцессный)')


